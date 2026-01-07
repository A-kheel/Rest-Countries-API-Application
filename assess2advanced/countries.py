import tkinter as tk
import requests
from PIL import Image, ImageTk, ImageEnhance
from io import BytesIO


root = tk.Tk()
root.title("Country Info App")
root.geometry("900x600")
root.resizable(0, 0)


base_url = "https://restcountries.com/v3.1/"

abrev = {
    "USA": "United States",
    "US": "United States",
    "UK": "United Kingdom",
    "UAE": "United Arab Emirates",
    "S. Korea": "South Korea",
    "N. Korea": "North Korea",
    "DRC": "Democratic Republic of the Congo",
    "CAR": "Central African Republic",
    "PRC": "China"
    }


flagimg = None        
flagimg2 = None      

def show_flag(url):
    global flagimg2, flagimg
    img_data = requests.get(url).content
    flagimg2 = Image.open(BytesIO(img_data))

    width = max(flagframe.winfo_width(), 300)
    height = max(flagframe.winfo_height(), 200)

    resized = flagimg2.resize((width, height), Image.LANCZOS)
    flagimg = ImageTk.PhotoImage(resized)
    flaglabel.config(image=flagimg)



def infos(data):
    official_name = data.get("name", {}).get("official", "N/A")
    common_name = data.get("name", {}).get("common", "N/A")
    capital = ", ".join(data.get("capital", ["N/A"]))
    population = data.get("population", "N/A")
    region = data.get("region", "N/A")

    population_text = f"{population:,}" if isinstance(population, int) else str(population)

    result.config(
        text=f"Official Name: {official_name}\n"
             f"Capital: {capital}\n"
             f"Population: {population_text}\n"
             f"Region: {region}"
    )

    languages = ", ".join(data.get("languages", {}).values()) or "N/A"

    currencies = data.get("currencies", {})
    if currencies:
        currency = ", ".join(f"{v.get('name','')} ({v.get('symbol','')})" for v in currencies.values())
    else:
        currency = "N/A"

    timezones = ", ".join(data.get("timezones", [])) or "N/A"

    result2.config(
        text=f"Languages: {languages}\n"
             f"Currency: {currency}\n"
             f"Timezones: {timezones}"
    )

    flag_url = data.get("flags", {}).get("png")
    if flag_url:
        show_flag(flag_url)
    else:
        flaglabel.config(image="")


def search_country():
    user_input = entry.get().strip()
    if not user_input:
        return

    
    country = abrev.get(user_input.upper(), user_input.strip())
    try:

        response = requests.get(f"{base_url}name/{country}?fullText=true")
        data = response.json()
        if isinstance(data, list) and data:
            infos(data[0])
        else:
            clear_labels()
    except Exception:
        clear_labels()

def clear_labels():
    result.config(text="country not found")
    result2.config(text="")
    flaglabel.config(image="")


bg = "flags.jpg"
bgimg = Image.open(bg).resize((900, 600))


bgimg = bgimg.convert("RGBA")

alpha = 0.6 
new_bg = Image.new("RGBA", bgimg.size, (255, 255, 255, 255)) 
bgimg = Image.blend(new_bg, bgimg, alpha)  


bgphoto = ImageTk.PhotoImage(bgimg)

bglabel = tk.Label(root, image=bgphoto)
bglabel.place(x=0, y=0, relwidth=1, relheight=1)

bgphoto = ImageTk.PhotoImage(bgimg)

bglabel = tk.Label(root, image=bgphoto)
bglabel.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(root, text="Country Search", font=("Calibri", 18, "bold"), bg="#ffffff").pack(pady=15)

entry = tk.Entry(root, width=35, font=("Calibri", 16))
entry.pack()
entry.focus()
entry.bind("<Return>", lambda event: search_country())

tk.Button(root, text="Search", font=("Calibri", 16), command=search_country).pack(pady=12)

stufframe = tk.Frame(root, bg="#ffffff")
stufframe.pack(pady=15, fill=tk.BOTH, expand=True)

info_frame = tk.Frame(stufframe, bg="#ffffff")
info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))

result = tk.Label(info_frame, font=("Calibri", 16), justify="left", bg="#ffffff", anchor="nw")
result.pack(fill=tk.BOTH, expand=True, pady=(0, 5))

result2 = tk.Label(info_frame,font=("Calibri", 16),justify="left",fg="gray20",bg="#ffffff",anchor="nw",wraplength=420)
result2.pack(fill=tk.BOTH, expand=True)

flagframe = tk.Frame(stufframe, bg="#ffffff")
flagframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

flaglabel = tk.Label(flagframe, bg="#ffffff")
flaglabel.pack(fill=tk.BOTH, expand=True)


root.mainloop()
