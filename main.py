from agents import Agent,Runner,OpenAIChatCompletionsModel,set_tracing_disabled
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
import asyncio
from get_products import get_product_data_from_sheet
from order import post_order_data_to_sheet
import streamlit as st 
from instructions import instruction

load_dotenv()
set_tracing_disabled(True)

API = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.5-flash"

external_client = AsyncOpenAI(
    api_key=API,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model=MODEL,
    openai_client=external_client
)

simple_Agent = Agent(
    name="Store Manager",
    instructions=instruction,
    model=model,
    tools=[get_product_data_from_sheet,post_order_data_to_sheet]
)

# Streamlit App
st.title("My Store.Com")


prompt = st.text_area("🔎 Search Products:")

if "history" not in st.session_state:
    st.session_state.history = []


if st.button("Search..."):
    with st.spinner("Thinking..."):
        st.session_state.history.append({"role": "user", "content": prompt})

        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        result = loop.run_until_complete(
            Runner.run(
                starting_agent=simple_Agent,
                input=st.session_state.history
            )
        )

        prompt = ""
        st.session_state.history.append({"role": "assistant", "content": result.final_output})

        st.success("Reply from Company Agent:")
        st.write(result.final_output)