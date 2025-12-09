# 📘 Prehistoric Planet – “Of All Time” Subtitle Analysis

A small Python project analyzing every subtitle phrase ending in **"of all time"** across *Prehistoric Planet* Season 3.
Built as an early prototype for **RewindOS**, a cultural-data toolkit for understanding patterns in TV, film, and streaming storytelling.

---

## 📌 Project Overview

Nature documentaries often lean on superlatives — *“the largest ever discovered,” “the biggest predator of all time,”* etc.
This project asks a simple, playful question:

> **How many times does Prehistoric Planet (Season 3) use the phrase “of all time,” and in what context?**

By extracting subtitle data and analyzing each occurrence of this phrase, we can begin to look at storytelling patterns through a quantitative lens — a small but illustrative example of the larger goals behind RewindOS.

---

## 🧠 How It Works

### 1. Subtitle Extraction

Season 3 SRT files were extracted from locally-owned media via VLC.
(Actual subtitle files **are not included** due to copyright.)

### 2. Regex Phrase Detection

A Python script scans all SRT files and detects any phrase ending with **"of all time"**, capturing up to 6 preceding words for context.

Core regex pattern:

```python
r"(\b\w+(?:\W+\w+){0,6}\W+of all time\b)"
```

### 3. Output

* Extracted phrases are printed to the console
* A CSV file of all detected phrases is saved to:

  ```
  data/of_all_time_results.csv
  ```

---

## 📂 Repository Structure

```
prehistoric-planet-of-all-time-analysis/
│
├── scripts/
│   └── biggest.py                  # Main extraction script
│
├── data/
│   └── of_all_time_results.csv     # Derived dataset (safe to publish)
│
├── samples/
│   └── sample_srt_snippet.srt      # Fake example of expected SRT formatting
│
├── .gitignore
├── LICENSE                         # MIT License
└── README.md
```

**Note: A private `srts/` folder (not included in the repo) contains the user's legally obtained SRT files.**


---

## 🛠 Requirements

* Python 3.8+
* A folder named `srts/` containing your own `.srt` subtitle files
* Basic familiarity with running Python scripts

---

## ▶️ Running the Script

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/prehistoric-planet-of-all-time-analysis.git
cd prehistoric-planet-of-all-time-analysis
```

### 2. Place your subtitle files in:

```
srts/
```

### 3. Run the extraction script

```bash
python scripts/biggest.py
```

### 4. View results

CSV output will be generated at:

```
data/of_all_time_results.csv
```

---

## 📊 Example Output (CSV)

```
file,snippet
Episode1.srt,biggest predator of all time
Episode3.srt,one of the most powerful hunters of all time
Episode5.srt,largest flying bird of all time
```

---

## 🧩 Why This Exists

This project represents a much larger vision:

### **RewindOS**

A cultural-intelligence platform for analyzing patterns in television, streaming, and storytelling using data-driven tools.

By starting with a phrase-level analysis, we create groundwork for:

* narrative motif tracking
* documentary superlative mapping
* actor presence analytics
* temporal storytelling trends
* episode-level linguistic insights

This simple script is a proof-of-concept showing how small datasets can reveal meaningful storytelling patterns.

---

## 📝 License

MIT License — free to use, modify, and share.

---

## 🙌 Acknowledgments

* Made with assistance from interactive AI workflowing
* Inspired by Apple TV+’s *Prehistoric Planet*
* Part of ongoing development for **RewindOS**
