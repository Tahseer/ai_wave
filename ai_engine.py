import os
import json
from groq import Groq

# Replace with your Groq API key
GROQ_API_KEY = "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"

groq_client = Groq(api_key=GROQ_API_KEY)
model_name = "llama3-70b-8192"

# AI function to parse user free text into structured JSON
def ask_ai(user_prompt):
    system_prompt = """
You are a trading assistant. Extract trading parameters from user request.

Always return ONLY valid JSON strictly like this:

{
  "symbol": "<symbol>",
  "timeframes": ["<timeframe1>", "<timeframe2>"],
  "indicators": ["<indicator1>", "<indicator2>"]
}

Supported indicators: EMA, MACD, RSI, Elliott Wave, Supertrend, Fibonacci, Ichimoku.

Detect if user says "Elliott", "Wave", "Supertrend", "Fibonacci", "Ichimoku" etc → map to indicators.

If user does not mention timeframes, default to ["1h", "4h", "1d"].
If symbol not mentioned, default to "BTCUSDT".
NEVER add extra text or explanation. Only return valid JSON.
"""

    response = groq_client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )

    json_text = response.choices[0].message.content
    return json.loads(json_text)

# Pine Script Deep Analyzer Generator
def generate_pine_script(symbol, timeframes, indicators):
    prompt = f"""
You are a highly advanced Pine Script v5 expert. Generate a full TradingView strategy script with deep analysis:

- Symbol: {symbol}
- Timeframes: {', '.join(timeframes)}
- Indicators: {', '.join(indicators)}

Requirements:

1. Use request.security for multi-timeframe calculations.
2. Combine indicators intelligently for strong trade signal generation.
3. Include clear BUY / SELL signal logic.
4. Add multi-condition confirmations.
5. Include entry, exit and stop-loss logic.
6. Generate alerts for important signals.
7. Use dynamic threshold filters for noise reduction.
8. Include volatility filters where possible.
9. Fully valid Pine Script v5 ONLY as output.

Example: If user asks for Elliott Wave, Fibonacci, EMA, Supertrend → combine into actionable trading strategy.

Output only valid Pine Script v5 code.
"""

    response = groq_client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content
