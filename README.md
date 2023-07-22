# Customer-Churn-Prediction-to-Improve-Retention-and-Reduce-Risk-of-Product-Discontinuation
Objective : untuk memprediksi customer yang akan berhenti dengan tujuan ingin meminimalisir resiko seorang customer untuk berhenti memakai produk yang di tawarkan

## Latar Belakang Masalah :
Dengan memahami pola churn, perusahaan dapat mengidentifikasi faktor-faktor yang berkontribusi pada tingkat churn yang tinggi, sehingga dapat mengambil keputusan strategis untuk meningkatkan retensi pelanggan.

## Data yang Digunakan :
Data ini berasal dari Hacktiv8 pada saat proses pembelajaran di Phase 2
Data ini terdiri dari 37010 baris dan 22 kolom dan terdapat missing value pada beberapa kolomnya

## Metode yang Digunakan :
metode yg digunakan adalah Deep Learning meliputi pembagian data menjadi train-test set menggunakan train_test_split, pembuatan pipeline untuk preprocessing data dengan make_pipeline, serta penggunaan Dense dan Dropout layers dalam pembuatan model neural network menggunakan Keras dan TensorFlow,
untuk melakukan customer segmentation dan memprediksi perilaku pelanggan berdasarkan data kartu kredit yang diberikan.


## Kelebihan Model:

- Peningkatan Performa: Setelah dilakukan improvement, baik model Sequential API maupun model Functional API mengalami peningkatan performa dengan nilai precision, recall, dan f1-score yang lebih baik. Hal ini menunjukkan bahwa model dapat memprediksi dengan lebih baik dan akurat.
- Fokus pada Customer Churn: Model ini memiliki fokus pada memprediksi risiko churn pada class 1 (customer yang berisiko berhenti memakai produk). Performa yang baik dalam mengklasifikasi class 1 (churn) menjadi kelebihan model ini karena dapat membantu perusahaan untuk mengidentifikasi pelanggan yang berisiko tinggi berhenti menggunakan produk dan mengambil tindakan pencegahan yang sesuai.
- Akurasi yang Tinggi: Model ini memiliki akurasi sebesar 86%, yang menunjukkan tingkat kesesuaian prediksi model dengan data yang sebenarnya. Akurasi yang tinggi merupakan kelebihan karena memperkuat kepercayaan perusahaan dalam menggunakan model ini untuk pengambilan keputusan.

## Kekurangan Model:

- Recall untuk Class 0 Rendah: Karena model lebih fokus pada prediksi class 1 (churn), nilai recall untuk class 0 (no churn) cenderung kecil. Hal ini berarti model mungkin kurang sensitif dalam mendeteksi customer yang tidak berisiko churn. Dalam konteks bisnis, kekurangan ini perlu diperhatikan karena risiko meninggalkan pelanggan yang tidak terdeteksi dapat mengakibatkan hilangnya pelanggan yang sebenarnya masih dapat dipertahankan.
- Perlu Improvisasi Lebih Lanjut: Meskipun model telah mengalami peningkatan performa, masih ada potensi untuk meningkatkan prediksi dengan melakukan improvisasi lebih lanjut. Proses optimasi model dapat melibatkan pemilihan hyperparameter yang lebih baik, eksplorasi arsitektur yang berbeda, atau penggunaan teknik lain untuk mengatasi masalah kelas yang tidak seimbang (misalnya, oversampling atau undersampling).

Customer Diversity: 
Mayoritas customer memiliki risiko churn yang rendah, tetapi masih ada sejumlah customer yang memiliki risiko churn yang tinggi. Model ini mungkin lebih menggambarkan kondisi mayoritas pelanggan dan perlu lebih diperhatikan dalam mengklasifikasi pelanggan yang berisiko tinggi untuk churn. Perusahaan perlu memperhatikan kelompok pelanggan dengan risiko churn yang tinggi dan mengambil tindakan khusus untuk meningkatkan retensi pada kelompok tersebut.

link deployment :
https://huggingface.co/spaces/nurulizzah/deployment_2

