
#  Text Summarization Using Hugging Face

A simple AI-powered text summarization web application built using **Python, Hugging Face Transformers, and Streamlit**. The application takes a long article or paragraph as input and generates a shorter summary.

##  Features

- Summarizes long articles and paragraphs using AI.
- Uses a pretrained Hugging Face summarization model.
- Provides Short, Medium, and Long summary length options.
- Displays the original and summarized word counts.
- Allows users to download the generated summary as a text file.
- Provides a simple, user-friendly web interface.

##  Technologies Used

- **Python** — Programming language
- **Hugging Face Transformers** — Pretrained AI summarization model
- **PyTorch** — Deep learning framework
- **Streamlit** — Web application interface

##  Project Structure

```text
text-summarization-app/
│
├── app.py
├── requirements.txt
├── README.md
└── .venv/
```

##  Installation and Setup

### 1. Clone the Repository

If your project is hosted on GitHub, run:

```bash
git clone https://github.com/lattikhashri178/Text-Summarization.git
cd text-summarization-app
```

Alternatively, open your existing project folder in VS Code.

### 2. Create a Virtual Environment

Python 3.10 is recommended for this setup.

```bash
py -3.10 -m venv .venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

##  Requirements

Create a file named `requirements.txt` with the following contents:

```text
streamlit>=1.40,<2.0
transformers>=4.45,<5.0
torch
```

##  Run the Application

In the VS Code terminal, execute:

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your web browser to use the application.

##  Model Used

**Model:** `sshleifer/distilbart-cnn-12-6`

This pretrained model is designed for summarizing news articles and other text. It is loaded using the Hugging Face `pipeline` API.

The model is downloaded automatically the first time it is used, so an internet connection is required for the initial download.

##  How to Use

1. Open the application in your browser.
2. Paste an article or paragraph into the text input area.
3. Select Short, Medium, or Long summary length.
4. Click **Generate Summary**.
5. Read the generated summary.
6. Download the summary as a `.txt` file if needed.

For best results, enter a reasonably long article with enough information to summarize.

##  Example

**Input:** An article explaining how artificial intelligence is transforming education, including personalized learning, teacher assistance, and challenges such as data privacy.

**Expected output:** A shorter paragraph highlighting the benefits of AI in education, its impact on teachers and students, and the importance of responsible use.

*Note: The generated summary depends on the input text and model output.*

##  Troubleshooting

### ModuleNotFoundError

Make sure your virtual environment is activated and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

### Summarization Pipeline Error

This project uses the Transformers 4.x summarization pipeline. Keep Transformers below version 5:

```bash
python -m pip install "transformers>=4.45,<5.0"
```

### Model Download Error

Check your internet connection and try running the application again.

### Streamlit Command Not Found

Run Streamlit through Python:

```bash
python -m streamlit run app.py
```

##  Future Improvements

- Support uploading text files and PDF documents.
- Add multilingual summarization.
- Provide more control over summary length.
- Improve the interface with additional customization options.

