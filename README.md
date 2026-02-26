# 🛒 Retail Sales Profitability Analysis

# 🔍 Proje Amacı
Superstore datasetini kullanarak satış ve kârlılık analizi yaptık.  
Hedef: Hangi kategori ve alt kategorilerin kâr marjı düşük, hangi stratejiler değiştirilmeli?



# 📊 Ana Bulgular

- **Toplam Satış:** 2,296,957  
- **Toplam Kar:** 286,324  

# Kategori Bazlı Kar Marjı
| Kategori          | Kar Marjı |
|------------------|-----------|
| Furniture         | 2.48% ❌ |
| Office Supplies   | 17.03% ✅ |
| Technology        | 17.40% ✅ |

# Furniture Alt Kategori Analizi
| Alt Kategori      | Kar        | Ortalama İndirim |
|------------------|-----------|----------------|
| Chairs           | 26,590    | 17%            |
| Furnishings      | 13,059    | 17%            |
| Bookcases        | -3,472    | 17%            |
| Tables           | -17,725   | 26% ❌         |

- Tables alt kategorisinde yüksek indirim uygulaması kârı ciddi şekilde düşürmüş.
- Bookcases alt kategorisinde indirimden dolayı kârı düşük ama tables kategorisinin yanında etkisiz kalıyor.



# 💡 İş Kararı Önerisi
- Tables indirim stratejisi gözden geçirilmeli  
- Yüksek indirimli ürünler segment bazlı analiz edilmeli  
- Zararlı SKU’lar portföyden çıkarılabilir  



 🧰 Kullanılan Teknolojiler
- Python  
- Pandas  
- Matplotlib  
- Seaborn  



 ▶ Nasıl Çalıştırılır
1. Pandas, Matplotlib ve Seaborn kütüphanesini yükle:  
```bash
pip install pandas matplotlib seaborn
