# Quantum Image Encryption and Decryption

## Introduction

This project presents a secure framework for image encryption and decryption using principles of quantum computing. It addresses the limitations of classical cryptographic techniques by leveraging quantum properties such as superposition and quantum key distribution (QKD).

The system ensures secure image transmission and accurate reconstruction using quantum-based encoding and encryption mechanisms.

---
## Key Features

* Quantum image representation using **NEQR (Novel Enhanced Quantum Representation)**
* Secure key exchange using **BB84 Quantum Key Distribution (QKD)**
* Encryption using quantum operations (XOR, CNOT, scrambling)
* Decryption via inverse quantum transformations
* High-fidelity image recovery with minimal data loss

---

## System Architecture

The system is divided into two main phases:

### 1. Encryption Phase

* Image acquisition and preprocessing
* NEQR-based quantum encoding
* Quantum key generation (BB84)
* Quantum encryption using gates and transformations

### 2. Decryption Phase

* Secure key reception
* Decryption using inverse operations
* Quantum measurement
* Image reconstruction

---
## Workflow

1. Input image is loaded and preprocessed
2. Image is encoded into quantum state using NEQR
3. Secure key is generated via BB84 protocol
4. Quantum encryption is applied
5. Encrypted data is transmitted
6. Decryption is performed using the shared key
7. Quantum measurement converts data to classical form
8. Original image is reconstructed

---
## Project Modules

* **Image Input Module** – Handles image loading and preprocessing
* **Quantum Encoding Module** – Converts image to quantum representation
* **Encryption Module** – Applies quantum encryption techniques
* **Key Distribution Module** – Implements BB84 protocol
* **Decryption Module** – Performs inverse operations
* **Measurement & Reconstruction Module** – Generates final output image

---
## Technologies Used

* Python 3.x
* Qiskit (IBM Quantum)
* NumPy
* Pillow
* Matplotlib

---
## System Requirements

### Software

* Python 3.10 or above
* Qiskit
* Jupyter Notebook / VS Code

### Hardware

* Minimum 8 GB RAM (16 GB recommended)
* Intel i5/i7 processor
* Stable internet connection

---
## Installation & Execution

### 1. Install Dependencies

```
pip install qiskit numpy pillow matplotlib
```

### 2. Run the Project

```
python main.py
```

### 3. Steps

* Provide input image
* System performs encoding and encryption
* Decrypted output is displayed

---
## Performance Metrics

* **PSNR (Peak Signal-to-Noise Ratio)** used to evaluate image quality
* High PSNR (> 40 dB) indicates successful reconstruction
* Minimal distortion between original and decrypted image

---

## Applications

* Secure image transmission systems
* Medical imaging security
* Military communication
* Cloud data protection

---

## Conclusion

This project demonstrates a practical approach to quantum-based image security. By integrating NEQR encoding with QKD, it provides a robust and future-ready encryption system that overcomes the vulnerabilities of classical methods.

---
## Authors

* Manasvi Rapolu
* Manikanta Suda
* Srishanth Legala
