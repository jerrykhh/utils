# Image to JPG

It will convert all image file to JPG, the following is more details 

Directory structure:
```
.
├── product1_id
|   ├── image1_name
|   ├── image2_name
└── product2_id
    ├── image1_name
    ├── image2_name
    └── image3_name

For example:
.
├── CLA-L01
│   ├── 0013_06_500x.jpg.webp
│   ├── 0014_05_500x.jpg.webp
│   ├── 1_b33467e1-59a2-4b52-8ecf-fa8330d1a792_1000x.jpg.webp
│   ├── 2_e130cb6f-d7d4-4d1d-8996-e6bd5a90a24f_1000x.jpg.webp
│   └── 3_4d179687-2d70-4ec9-bcf6-441443a5f7e0_1000x.jpg.webp
├── CLF-500
│   ├── CLF500LGClaymore3FaceMiniLightGrey01_700x_1_960x.jpg.webp
│   └── CLF500LGClaymore3FaceMiniLightGrey_1080x.jpg.webp
└── ST-941
    ├── 1_154e26ec-f773-42ac-9c04-a08be2a6a37c_700x.jpg.webp
    ├── 2_cde01734-94c6-4376-9528-dd0e31b150cd_700x.jpg.webp
    ├── 3_1b438112-0c7f-4d71-b4e7-6369a4d67157_700x.jpg.webp
    └── h0223001_4953571079417_180830112403_01_515.jpg

Result:
├── CLA-L01
│   ├── CLA-L01-asdd123.jpg
│   ├── CLA-L01-f77agh3.jpg
│   ├── CLA-L01-b4e7asd.jpg
│   ├── CLA-L01-asjn123.jpg
│   └── CLA-L01-asddf13.jpg
├── CLF-500
│   ├── CLF-500-asdzxd.jpg
│   └── CLF-500-aytdjd.jpg
└── ST-941
    ├── ST-941-asdj9u4.jpg
    ├── ST-941-dfgfsd3.jpg
    ├── ST-941-assdgaf.jpg
    └── ST-941-asdsdf4.jpg

```

## Usage
```
python convert.py '/Users/jerrykwok/Downloads/products_img/'
```