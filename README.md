# 📥 Instagram Post Downloader

A simple and straightforward Python script to download **public Instagram posts** using either the post URL or its shortcode.  
Built with [Instaloader](https://instaloader.github.io/).

---

## 📌 Features

- 📸 Download **photos** and **videos** from public Instagram posts  
- 🎞️ Supports **carousel posts** (multiple images or videos)  
- 🖼️ Downloads **video thumbnails (covers)**  
- 📝 Downloads the **post caption (description)** as a `.txt` file  
- 📑 Saves **post metadata** in a **zipped** `.json` file  
- 💾 Stores everything in a local `downloads/` folder  

---

## 🛠️ Requirements

- Python **3.8+**
- [Instaloader](https://pypi.org/project/instaloader/)

To install the required package:

```bash
pip install instaloader
