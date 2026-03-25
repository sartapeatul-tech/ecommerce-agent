#!/bin/bash

echo "Building index..."
python app/rag/build_index.py

echo "Starting UI..."
streamlit run app/ui/streamlit_app.py