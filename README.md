# KiPiZK - Remove Background Gratis

Website untuk menghapus background gambar secara otomatis menggunakan AI. 100% gratis, tanpa iklan, akurasi tinggi.

## Fitur

- ✅ Remove background otomatis dengan AI (RMBG Model)
- ✅ Upload gambar (drag & drop / click)
- ✅ Preview original vs hasil
- ✅ Download PNG transparent
- ✅ Akurasi tinggi untuk semua object (manusia, produk, hewan, dll)
- ✅ UI dark minimalis elegan
- ✅ Responsive mobile-friendly

## Teknologi

### Frontend
- HTML/CSS/JavaScript (Vanilla)
- Dark minimalist UI inspired by remove.bg
- Google Fonts (Inter)

### Backend
- Python 3.9+
- rembg library (U2-Net model)
- Vercel Serverless Functions

## Deploy

### Requirements
- Vercel account
- GitHub repository

### Deploy Steps

1. Push code ke GitHub:
```bash
git add .
git commit -m "Update with backend API"
git push origin main
```

2. Connect ke Vercel:
- Login https://vercel.com
- Import dari GitHub: ekikieee/kipizk
- Auto-deploy

3. Vercel akan otomatis detect Python serverless function

## Development

### Local Testing (Frontend only)
```bash
python -m http.server 8000
```

### Local Testing (With Backend)
```bash
pip install -r requirements.txt
vercel dev
```

## Architecture

- **Frontend**: Static HTML/CSS/JS hosted on Vercel CDN
- **Backend**: Python serverless function `/api/remove-bg`
- **Model**: rembg with U2-Net (high accuracy segmentation)

## License

MIT
