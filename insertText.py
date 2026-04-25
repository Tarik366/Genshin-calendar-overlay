import tkinter as tk
from tkinter import font as tkfont

def char_in_font(char: str, font_obj: tkfont.Font) -> bool:
    """
    Karakterin font'ta tanımlı olup olmadığını tahmin eder.
 
    Kural:
      - Ölçülen genişlik 0 ise → yok
      - Genişlik, tofu kutusununkiyle aynıysa → muhtemelen yok
        (ve karakter tofu karakterinin kendisi değilse)
    """
    width = font_obj.measure(char)
    if width == 0:
        return False
    tofu = _tofu_width(font_obj)
    if tofu > 0 and width == tofu and char != "\uFFFE":
        return False
    return True


def insert_with_fallback(
    text_widget: tk.Text,
    text: str,
    primary_font: tkfont.Font,
    fallback_font: tkfont.Font,
    index: str = tk.END,
):
    """
    `text` içindeki her karakteri inceler:
      - Birincil font'ta varsa  → 'pf_tag'  etiketiyle ekler
      - Birincil font'ta yoksa  → 'fb_tag'  etiketiyle (fallback) ekler
 
    Aynı etikete sahip ardışık karakterler tek seferde eklenir
    (performans için segmentlere ayırma).
    """
    # Etiketleri bir kez yapılandır (tekrar çağrılabilir, üzerine yazar)
    text_widget.tag_configure("pf_tag", font=primary_font)
    text_widget.tag_configure("fb_tag", font=fallback_font)
 
    segment = ""
    current_tag = None
 
    for ch in text:
        tag = "pf_tag" if char_in_font(ch, primary_font) else "fb_tag"
 
        if tag == current_tag:
            segment += ch
        else:
            if segment:
                text_widget.insert(index, segment, current_tag)
            segment = ch
            current_tag = tag
 
    if segment:
        text_widget.insert(index, segment, current_tag)
