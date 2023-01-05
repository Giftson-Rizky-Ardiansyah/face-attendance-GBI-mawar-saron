import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-369e7-default-rtdb.firebaseio.com/"
    
})

ref = db.reference('Data Masuk')

data = {
    "321654": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 10:39:00",
      "Wilayah_Komsel": "G",
      "name": "Murtaza Hassan",
      "total_absen": 13
    },
    "963852": {
      "Bidang": "Economics",
      "KAJ": 2021,
      "Nomor_Telpon": 1,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "B",
      "name": "Elon Musk",
      "total_absen": 12
    },
    "Agnes Tantini": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Agnes Tantini",
      "total_absen": 7
    },
    "Anathasya AZ Junus": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:26:50",
      "Wilayah_Komsel": "G",
      "name": "Anathasya A.Z. Junus",
      "total_absen": 8
    },
    "Anathasya Angelie": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:27:00",
      "Wilayah_Komsel": "G",
      "name": "Anathasya Angelie",
      "total_absen": 8
    },
    "Andi Slamet": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Andi Slamet",
      "total_absen": 7
    },
    "Antonius Ruben": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:25:48",
      "Wilayah_Komsel": "G",
      "name": "Antonius Ruben",
      "total_absen": 10
    },
    "Apriana Christanty": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:42:26",
      "Wilayah_Komsel": "G",
      "name": "Apriana Christanty",
      "total_absen": 10
    },
    "Aprina Mega H": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Aprina Mega H",
      "total_absen": 7
    },
    "Arista Karuku Utang": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Arista Karuku Utang",
      "total_absen": 7
    },
    "Arnold Talahatu": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Arnold Talahatu",
      "total_absen": 7
    },
    "Aurelia Elisabeth": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:08:03",
      "Wilayah_Komsel": "G",
      "name": "Aurelia Elisabeth",
      "total_absen": 9
    },
    "Ave Gunawan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Ave Gunawan",
      "total_absen": 7
    },
    "B Dwi Handoko": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "B. Dwi Handoko",
      "total_absen": 7
    },
    "Bambang Sri Partono": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Bambang Sri Partono",
      "total_absen": 7
    },
    "Basaria Siregar": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:09:24",
      "Wilayah_Komsel": "G",
      "name": "Basaria Siregar",
      "total_absen": 8
    },
    "Bernard Simbolon": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:03:50",
      "Wilayah_Komsel": "G",
      "name": "Bernard Simbolon",
      "total_absen": 8
    },
    "Berta Purba": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:04:51",
      "Wilayah_Komsel": "G",
      "name": "Berta Purba",
      "total_absen": 9
    },
    "Betsyeba Torong": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Betsyeba Torong",
      "total_absen": 7
    },
    "Binsar Parulian": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 13:04:03",
      "Wilayah_Komsel": "G",
      "name": "Binsar Parulian",
      "total_absen": 9
    },
    "Budiman Nainggolan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Budiman Nainggolan",
      "total_absen": 7
    },
    "Carolina": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Carolina",
      "total_absen": 7
    },
    "Charly Nayoan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:27:30",
      "Wilayah_Komsel": "G",
      "name": "Charly Nayoan",
      "total_absen": 11
    },
    "Chendra Mustika": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:08:26",
      "Wilayah_Komsel": "G",
      "name": "Chendra Mustika",
      "total_absen": 8
    },
    "Danny M Kasenda": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 10:38:53",
      "Wilayah_Komsel": "G",
      "name": "Danny M. Kasenda",
      "total_absen": 8
    },
    "Darsini": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Darsini",
      "total_absen": 7
    },
    "Deny Monintja": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Deny Monintja",
      "total_absen": 7
    },
    "Desi Aprilia": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:07:18",
      "Wilayah_Komsel": "G",
      "name": "Desi Aprilia",
      "total_absen": 8
    },
    "Dewi Sundari": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Dewi Sundari",
      "total_absen": 7
    },
    "Dina Margaretha": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Dina Margaretha",
      "total_absen": 7
    },
    "Dita Ongko": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:33:02",
      "Wilayah_Komsel": "G",
      "name": "Dita Ongko",
      "total_absen": 10
    },
    "Eddy R Torong": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:21:30",
      "Wilayah_Komsel": "G",
      "name": "Eddy R. Torong",
      "total_absen": 10
    },
    "Edward H Purba": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:27:17",
      "Wilayah_Komsel": "G",
      "name": "Edward H. Purba",
      "total_absen": 11
    },
    "Eiverth Crison T": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:06:17",
      "Wilayah_Komsel": "G",
      "name": "Eiverth Crison. T",
      "total_absen": 8
    },
    "Eko B Prabowo": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Eko B. Prabowo",
      "total_absen": 7
    },
    "Eko Januyanti": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:27:04",
      "Wilayah_Komsel": "G",
      "name": "Eko Januyanti",
      "total_absen": 8
    },
    "Elisabeth Kanaf": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Elisabeth Kanaf",
      "total_absen": 7
    },
    "Endang Susilowati": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Endang Susilowati",
      "total_absen": 7
    },
    "Erik S Sinuhaji": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:10:47",
      "Wilayah_Komsel": "G",
      "name": "Erik S. Sinuhaji",
      "total_absen": 8
    },
    "Erty Rumany": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Erty Rumany",
      "total_absen": 7
    },
    "Esra Lumban Gaol": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:10:24",
      "Wilayah_Komsel": "G",
      "name": "Esra Lumban Gaol",
      "total_absen": 8
    },
    "Esther D": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:14:28",
      "Wilayah_Komsel": "G",
      "name": "Esther D",
      "total_absen": 9
    },
    "Etti Manurung": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Etti Manurung",
      "total_absen": 7
    },
    "Evi Sjiane": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 10:35:27",
      "Wilayah_Komsel": "G",
      "name": "Evi Sjiane",
      "total_absen": 8
    },
    "Ewiwati": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Ewiwati",
      "total_absen": 7
    },
    "Faisal Ashari": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Faisal Ashari",
      "total_absen": 7
    },
    "Franky P": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:10:39",
      "Wilayah_Komsel": "G",
      "name": "Franky P",
      "total_absen": 8
    },
    "Fransina Ludji": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Fransina Ludji",
      "total_absen": 7
    },
    "Fransiskus Berkanis": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:37:09",
      "Wilayah_Komsel": "G",
      "name": "Fransiskus Berkanis",
      "total_absen": 9
    },
    "Fridianus Saragih": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:25:57",
      "Wilayah_Komsel": "G",
      "name": "Fridianus Saragih",
      "total_absen": 9
    },
    "Gatot Antonius": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Gatot Antonius",
      "total_absen": 7
    },
    "Gerards R Lubis": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:30:14",
      "Wilayah_Komsel": "G",
      "name": "Gerards R. Lubis",
      "total_absen": 12
    },
    "Gordhes Roni P": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Gordhes Roni P.",
      "total_absen": 7
    },
    "Gretha Cherley": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Gretha Cherley",
      "total_absen": 7
    },
    "Gunawan Joesoep": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Gunawan Joesoep",
      "total_absen": 7
    },
    "H Petrus Sihombing": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "H. Petrus Sihombing",
      "total_absen": 7
    },
    "Hani Marlina": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:10:08",
      "Wilayah_Komsel": "G",
      "name": "Hani Marlina",
      "total_absen": 8
    },
    "Hendra A Sinaga": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Hendra A. Sinaga",
      "total_absen": 7
    },
    "Hendra Ongko": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:01:54",
      "Wilayah_Komsel": "G",
      "name": "Hendra Ongko",
      "total_absen": 8
    },
    "Hendry Panjaitan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Hendry Panjaitan",
      "total_absen": 7
    },
    "Hengdra": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Hengdra",
      "total_absen": 7
    },
    "Henry Kurniawan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Henry Kurniawan",
      "total_absen": 7
    },
    "Herman Gunawan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-29 08:13:33",
      "Wilayah_Komsel": "G",
      "name": "Herman Gunawan",
      "total_absen": 11
    },
    "Hotmauli Panjaitan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Hotmauli Panjaitan",
      "total_absen": 7
    },
    "Hotni Simamora": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Hotni Simamora",
      "total_absen": 7
    },
    "IMG20220926163828": {
      "Bidang": "Pelayanan",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-29 08:18:34",
      "Wilayah_Komsel": "G",
      "name": "Rizky Ardiansyah",
      "total_absen": 37
    },
    "Ingeralda V": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:23:57",
      "Wilayah_Komsel": "G",
      "name": "Ingeralda V",
      "total_absen": 8
    },
    "Irianto Hutauruk": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Irianto Hutauruk",
      "total_absen": 7
    },
    "Irwan Siddharta": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:00:15",
      "Wilayah_Komsel": "G",
      "name": "Irwan Siddharta",
      "total_absen": 8
    },
    "Isak Kanaf": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Isak Kanaf",
      "total_absen": 7
    },
    "Isto KR Anding": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:16:14",
      "Wilayah_Komsel": "G",
      "name": "Isto K.R. Anding",
      "total_absen": 8
    },
    "Jacob Wattimury": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Jacob Wattimury",
      "total_absen": 7
    },
    "Jafar S Silitonga": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:21:19",
      "Wilayah_Komsel": "G",
      "name": "Jafar S. Silitonga",
      "total_absen": 8
    },
    "Jahja Nicolas": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:22:53",
      "Wilayah_Komsel": "G",
      "name": "Jahja Nicolas",
      "total_absen": 10
    },
    "Jap Erti": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Jap Erti",
      "total_absen": 7
    },
    "Jaspen Marpaung": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Jaspen Marpaung",
      "total_absen": 7
    },
    "Jori Mangensihi": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-29 08:13:10",
      "Wilayah_Komsel": "G",
      "name": "Jori Mangensihi",
      "total_absen": 10
    },
    "Junus": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Junus",
      "total_absen": 7
    },
    "Kadim Tarigan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Kadim Tarigan",
      "total_absen": 7
    },
    "Kastini Br Sebayang": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Kastini Br Sebayang",
      "total_absen": 7
    },
    "Lanny Obaya": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:15:36",
      "Wilayah_Komsel": "G",
      "name": "Lanny Obaya",
      "total_absen": 9
    },
    "Lea Lobo": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:00:33",
      "Wilayah_Komsel": "G",
      "name": "Lea Lobo",
      "total_absen": 8
    },
    "Lena Raduck": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:19:19",
      "Wilayah_Komsel": "G",
      "name": "Lena Raduck",
      "total_absen": 10
    },
    "Leny Setyawati": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:09:54",
      "Wilayah_Komsel": "G",
      "name": "Leny Setyawati",
      "total_absen": 8
    },
    "Lidia L Samosir": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Lidia L. Samosir",
      "total_absen": 7
    },
    "Lidya Swantika": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Lidya Swantika",
      "total_absen": 7
    },
    "Linda TB Hasibuan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-29 08:14:58",
      "Wilayah_Komsel": "G",
      "name": "Linda TB Hasibuan",
      "total_absen": 15
    },
    "Lisberia Sinaga": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Lisberia Sinaga",
      "total_absen": 7
    },
    "Lusia Sri Suciati": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Lusia Sri Suciati",
      "total_absen": 7
    },
    "Magda Korua": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Magda Korua",
      "total_absen": 7
    },
    "Mangita Sihite": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:26:24",
      "Wilayah_Komsel": "G",
      "name": "Mangita Sihite",
      "total_absen": 9
    },
    "Marchelinus": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:33:29",
      "Wilayah_Komsel": "G",
      "name": "Marchelinus",
      "total_absen": 8
    },
    "Maria Ave": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Maria Ave",
      "total_absen": 7
    },
    "Maria Dalmo": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Maria Dalmo",
      "total_absen": 7
    },
    "Maria M Dethan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:20:25",
      "Wilayah_Komsel": "G",
      "name": "Maria M. Dethan",
      "total_absen": 8
    },
    "Maria M Tampubolon": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:10:03",
      "Wilayah_Komsel": "G",
      "name": "Maria M. Tampubolon",
      "total_absen": 8
    },
    "Mariana": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-29 08:15:08",
      "Wilayah_Komsel": "G",
      "name": "Mariana",
      "total_absen": 9
    },
    "Mei Siregar": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:32:10",
      "Wilayah_Komsel": "G",
      "name": "Mei Siregar",
      "total_absen": 8
    },
    "Melani Kariri Hara": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Melani Kariri Hara",
      "total_absen": 7
    },
    "Melani WB": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:10:54",
      "Wilayah_Komsel": "G",
      "name": "Melani WB.",
      "total_absen": 8
    },
    "Melly Gresia": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:05:57",
      "Wilayah_Komsel": "G",
      "name": "Melly Gresia",
      "total_absen": 14
    },
    "Meryon Hutabalian": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:19:56",
      "Wilayah_Komsel": "G",
      "name": "Meryon Hutabalian",
      "total_absen": 8
    },
    "Mesli Manurung": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:05:17",
      "Wilayah_Komsel": "G",
      "name": "Mesli Manurung",
      "total_absen": 11
    },
    "Michael Lontaan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Michael Lontaan",
      "total_absen": 7
    },
    "Michael Palbe": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:26:30",
      "Wilayah_Komsel": "G",
      "name": "Michael Palbe",
      "total_absen": 11
    },
    "Nani": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:15:10",
      "Wilayah_Komsel": "G",
      "name": "Nani",
      "total_absen": 9
    },
    "Nurcahya Hutapea": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Nurcahya Hutapea",
      "total_absen": 7
    },
    "Nurlena Rismawati": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Nurlena Rismawati",
      "total_absen": 7
    },
    "Oey Tanto P": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Oey Tanto P",
      "total_absen": 7
    },
    "P Rajagukguk": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:03:14",
      "Wilayah_Komsel": "G",
      "name": "P. Rajagukguk",
      "total_absen": 8
    },
    "Parolan Sinaga": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 13:00:44",
      "Wilayah_Komsel": "G",
      "name": "Parolan Sinaga",
      "total_absen": 11
    },
    "Patar L Tobing": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Patar L. Tobing",
      "total_absen": 7
    },
    "Patrick Fatruan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:16:36",
      "Wilayah_Komsel": "G",
      "name": "Patrick Fatruan",
      "total_absen": 8
    },
    "Paula Elyana": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Paula Elyana",
      "total_absen": 7
    },
    "Paula Longkutoy": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Paula Longkutoy",
      "total_absen": 7
    },
    "Phoeng Jan Nie": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:15:55",
      "Wilayah_Komsel": "G",
      "name": "Phoeng Jan Nie",
      "total_absen": 8
    },
    "Pin Pin": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Pin Pin",
      "total_absen": 7
    },
    "Pinta Lasmarito": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Pinta Lasmarito",
      "total_absen": 7
    },
    "Pinta Uli S": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Pinta Uli S",
      "total_absen": 7
    },
    "Pomi Sinaga": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Pomi Sinaga",
      "total_absen": 7
    },
    "Prasetya Dewi": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:12:08",
      "Wilayah_Komsel": "G",
      "name": "Prasetya Dewi",
      "total_absen": 9
    },
    "Priscilla Maria R": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:16:03",
      "Wilayah_Komsel": "G",
      "name": "Priscilla Maria R",
      "total_absen": 8
    },
    "Ramayanti Yeni": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:37:17",
      "Wilayah_Komsel": "G",
      "name": "Ramayanti Yeni",
      "total_absen": 8
    },
    "Ramli Sanjaya": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:03:33",
      "Wilayah_Komsel": "G",
      "name": "Ramli Sanjaya",
      "total_absen": 8
    },
    "Reinheart MR": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:08:56",
      "Wilayah_Komsel": "G",
      "name": "Reinheart M.R.",
      "total_absen": 8
    },
    "Rejeki veranita": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:17:47",
      "Wilayah_Komsel": "G",
      "name": "Rejeki veranita",
      "total_absen": 9
    },
    "Ria NS": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:25:03",
      "Wilayah_Komsel": "G",
      "name": "Ria N.S.",
      "total_absen": 9
    },
    "Rohani T": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Rohani T",
      "total_absen": 7
    },
    "Rotua Risma": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Rotua Risma",
      "total_absen": 7
    },
    "Roylan Pasaribu": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Roylan Pasaribu",
      "total_absen": 7
    },
    "Rudi Legi": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Rudi Legi",
      "total_absen": 7
    },
    "Rudy H Sitorus": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:18:24",
      "Wilayah_Komsel": "G",
      "name": "Rudy H. Sitorus",
      "total_absen": 8
    },
    "Rusman Hutahaean": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Rusman Hutahaean",
      "total_absen": 7
    },
    "Sabar Gunawan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Sabar Gunawan",
      "total_absen": 7
    },
    "Sabungan Sibarani": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Sabungan Sibarani",
      "total_absen": 7
    },
    "Sadilah": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:34:01",
      "Wilayah_Komsel": "G",
      "name": "Sadilah",
      "total_absen": 11
    },
    "Samson Sitohang": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Samson Sitohang",
      "total_absen": 7
    },
    "Sano": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Sano",
      "total_absen": 7
    },
    "Saor Simorangkir": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Saor Simorangkir",
      "total_absen": 7
    },
    "Sarah Samosir": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Sarah Samosir",
      "total_absen": 7
    },
    "Saud Mangasi": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Saud Mangasi",
      "total_absen": 7
    },
    "Selvi Liando": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Selvi Liando",
      "total_absen": 7
    },
    "Setia Ningsih": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Setia Ningsih",
      "total_absen": 7
    },
    "Sici Lewi Masleni": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Sici Lewi Masleni",
      "total_absen": 7
    },
    "Siti Heryani": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-29 08:15:32",
      "Wilayah_Komsel": "G",
      "name": "Siti Heryani",
      "total_absen": 8
    },
    "Sri Muntingah": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Sri Muntingah",
      "total_absen": 7
    },
    "Sri S Simanjuntak": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Sri S. Simanjuntak",
      "total_absen": 7
    },
    "Srikoning W": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Srikoning W",
      "total_absen": 7
    },
    "Sugiyanmi": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Sugiyanmi",
      "total_absen": 7
    },
    "Sujanto": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Sujanto",
      "total_absen": 7
    },
    "Suryani Hutajulu": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:04:39",
      "Wilayah_Komsel": "G",
      "name": "Suryani Hutajulu",
      "total_absen": 8
    },
    "Susianti Buha": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Susianti Buha",
      "total_absen": 7
    },
    "Suwarti": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Suwarti",
      "total_absen": 7
    },
    "Tan Linda CW": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-29 08:12:01",
      "Wilayah_Komsel": "G",
      "name": "Tan Linda C.W",
      "total_absen": 8
    },
    "Tetty Nainggolan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:24:27",
      "Wilayah_Komsel": "G",
      "name": "Tetty Nainggolan",
      "total_absen": 8
    },
    "Theo E Pupella": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-29 08:13:17",
      "Wilayah_Komsel": "G",
      "name": "Theo E Pupella",
      "total_absen": 8
    },
    "Tiur Lan": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Tiur Lan",
      "total_absen": 7
    },
    "Tonny Wongkar": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:35:26",
      "Wilayah_Komsel": "G",
      "name": "Tonny Wongkar",
      "total_absen": 9
    },
    "Tursinah": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:19:41",
      "Wilayah_Komsel": "G",
      "name": "Tursinah",
      "total_absen": 9
    },
    "Victor Maruli S": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 13:04:06",
      "Wilayah_Komsel": "G",
      "name": "Victor Maruli S",
      "total_absen": 10
    },
    "WZ Natalia": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-29 08:15:01",
      "Wilayah_Komsel": "G",
      "name": "W.Z. Natalia",
      "total_absen": 9
    },
    "Wempi H Roring": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:18:15",
      "Wilayah_Komsel": "G",
      "name": "Wempi H. Roring",
      "total_absen": 10
    },
    "Wilson Sinaga": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Wilson Sinaga",
      "total_absen": 7
    },
    "Yang Tjik": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Yang Tjik",
      "total_absen": 7
    },
    "Yanto Effendy": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Yanto Effendy",
      "total_absen": 7
    },
    "Yenny Dorince": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-29 08:12:20",
      "Wilayah_Komsel": "G",
      "name": "Yenny Dorince",
      "total_absen": 8
    },
    "Yerni Budiman": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-11 00:54:34",
      "Wilayah_Komsel": "G",
      "name": "Yerni Budiman",
      "total_absen": 7
    },
    "Yohanes Kasminto": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 13:04:18",
      "Wilayah_Komsel": "G",
      "name": "Yohanes Kasminto",
      "total_absen": 8
    },
    "Yuli Antonius": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:33:12",
      "Wilayah_Komsel": "G",
      "name": "Yuli Antonius",
      "total_absen": 9
    },
    "Yuni Fauziana": {
      "Bidang": "Pelayanan Ibadah",
      "KAJ": 2017,
      "Nomor_Telpon": 4,
      "Waktu_Absen_Terakhir": "2022-12-24 12:04:31",
      "Wilayah_Komsel": "G",
      "name": "Yuni Fauziana",
      "total_absen": 8
    }
  }

for key, value in data.items():
    ref.child(key).set(value)
