# SVG Certificate Generator

This is a lightweight SVG-based certificate template designer and generator built using **Flask** and **SVG-Edit**. It allows any issuing authority to:

* 🎨 Design certificate templates visually using SVG (with placeholders like `{{name}}`, `{{course}}`, etc.)
* 📝 Fill in dynamic form data
* 📄 Generate and download PDF certificates via browser

---

## 📁 Folder Structure

```
project/
├── app.py                           # Flask backend for handling template, data fill, and PDF generation
├── static/
│   ├── editor.html                  # UI for SVG-Edit embedded in iframe
│   ├── form.html                    # Form UI to fill certificate details
│   ├── template.svg                 # Sample SVG template with placeholders
│   ├── filled_certificate.svg       # (auto-generated after filling)
│   ├── svgedit/                     # Full SVG-Edit tool copied locally
│   └── generated_certificates/      # Output folder for final PDF
└── requirements.txt                # Python package dependencies
```

---

## 🚀 How to Run

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd svg-certificate-generator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the Server

```bash
python3 app.py
```

It will start on `http://127.0.0.1:5000`, or your public URL in Codespace.

---

## ✨ How to Use

### 1. Design Certificate Template

* Visit `/` → opens **SVG-Edit** UI
* Add text with placeholders like: `{{name}}`, `{{course}}`, `{{date}}`
* Save using "💾 Save Template" button

### 2. Fill Form and Generate

* Visit `/form`
* Fill in the values for `name`, `course`, `date`
* Click "📄 Create Certificate"
* Auto-download of generated PDF starts

### Integration with external code
* Here certificate is genretaed by calling form page on browser and then filling information, but same inputs can be given by passing parameters from backend where source can be any other API
---

## ⚙️ Endpoints Summary

| Endpoint                | Method | Purpose                              |
| ----------------------- | ------ | ------------------------------------ |
| `/`                     | GET    | SVG Editor UI                        |
| `/upload-template`      | POST   | Save SVG template with placeholders  |
| `/form`                 | GET    | Form UI to enter certificate details |
| `/generate-certificate` | POST   | Accepts form or JSON, returns PDF    |

---

## ✅ Sample Placeholder Tags in SVG

Use these tags anywhere in the template:

```xml
<text>{{name}}</text>
<text>{{course}}</text>
<text>{{date}}</text>
```

These get replaced when generating certificate.

---

## 📦 Requirements

```
Flask
cairosvg
```

Install via:

```bash
pip install -r requirements.txt
```

---

## 🧠 Notes for Integration Team

* You can embed the `/form` endpoint in an iframe inside your system
* Or use `/generate-certificate` directly from frontend using `fetch` or Axios POST
* This project is modular and supports integration with APIs, Excel uploads, email sending, etc.

For any dynamic features, placeholders can be extended easily.

---

## 🧩 Planned Enhancements (Optional)

* Auto-detect placeholders from SVG and dynamically build form
* Certificate preview before download
* Bulk generation from CSV
* Email-to-receivers directly

---

## 👨‍💻 Contact

Project maintained by: Prashant.Malviya@wadhwanifoundation.org

For queries or enhancements, raise an issue or ping on email/Slack.
