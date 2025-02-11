import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
file_path = 'data/most_popular_1000_youtube_videos.csv'
data = pd.read_csv(file_path)

# Pembersihan Data
# Menghapus tanda koma dari kolom numerik dan mengubahnya menjadi integer
data['Video views'] = data['Video views'].str.replace(',', '').astype(int)
data['Likes'] = data['Likes'].str.replace(',', '').astype(int)
data['Dislikes'] = data['Dislikes'].fillna('0').str.replace(',', '').astype(int)

# Menghapus baris dengan nilai yang hilang
data.dropna(inplace=True)

# Analisis Statistik Deskriptif per Kategori
category_stats = data.groupby('Category').agg({
    'Video views': ['mean', 'sum', 'count'],
    'Likes': ['mean', 'sum'],
    'Dislikes': ['mean', 'sum']
}).reset_index()

# Rename columns for better readability
category_stats.columns = ['Category', 'Avg Views', 'Total Views', 'Total Videos', 'Avg Likes', 'Total Likes', 'Avg Dislikes', 'Total Dislikes']

# Tampilkan tabel statistik per kategori
print("Statistik per Kategori:")
print(category_stats)

# Visualisasi Data

# 1. Bar Chart untuk Rata-rata Views per Kategori
plt.figure(figsize=(14, 8))
sns.barplot(x='Category', y='Avg Views', data=category_stats, palette='viridis')
plt.title('Rata-rata Views per Kategori')
plt.xlabel('Kategori')
plt.ylabel('Rata-rata Views')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar Chart untuk Rata-rata Likes per Kategori
plt.figure(figsize=(14, 8))
sns.barplot(x='Category', y='Avg Likes', data=category_stats, palette='plasma')
plt.title('Rata-rata Likes per Kategori')
plt.xlabel('Kategori')
plt.ylabel('Rata-rata Likes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Bar Chart untuk Rata-rata Dislikes per Kategori
plt.figure(figsize=(14, 8))
sns.barplot(x='Category', y='Avg Dislikes', data=category_stats, palette='magma')
plt.title('Rata-rata Dislikes per Kategori')
plt.xlabel('Kategori')
plt.ylabel('Rata-rata Dislikes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Bar Chart untuk Total Views per Kategori
plt.figure(figsize=(14, 8))
sns.barplot(x='Category', y='Total Views', data=category_stats, palette='coolwarm')
plt.title('Total Views per Kategori')
plt.xlabel('Kategori')
plt.ylabel('Total Views')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Bar Chart untuk Total Likes per Kategori
plt.figure(figsize=(14, 8))
sns.barplot(x='Category', y='Total Likes', data=category_stats, palette='cividis')
plt.title('Total Likes per Kategori')
plt.xlabel('Kategori')
plt.ylabel('Total Likes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Bar Chart untuk Total Dislikes per Kategori
plt.figure(figsize=(14, 8))
sns.barplot(x='Category', y='Total Dislikes', data=category_stats, palette='YlOrBr')
plt.title('Total Dislikes per Kategori')
plt.xlabel('Kategori')
plt.ylabel('Total Dislikes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7. Pie Chart untuk Jumlah Video per Kategori
plt.figure(figsize=(10, 8))
plt.pie(category_stats['Total Videos'], labels=category_stats['Category'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set3'))
plt.title('Jumlah Video per Kategori')
plt.tight_layout()
plt.show()
