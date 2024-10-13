NEO: Novel Epitope Optimizer
Nishanth Basava

As cancer cases continue to rise, with a 2023 study from Zhejiang and Harvard predicting a 31% increase in cases and a 21% increase in deaths by 2030, the need to find more effective treatments for cancer is greater than ever before. Traditional approaches to treating cancer, such as chemotherapy, often kill healthy cells because of their lack of targetability. On the contrary, personalized cancer vaccines can utilize neoepitopes - distinctive peptides on cancer cells that are often missed by the body’s immune system - that have strong binding affinities to a patient’s MHC to provide a more targeted treatment approach. The selection of the perfect neoepitopes that elicit an immune response is a time-consuming and costly process because of the required inputs of modern predictive methods. This project aims to facilitate faster, cheaper, and more accurate neoepitope binding predictions with the use of Feed Forward Neural Networks and Recurrent Neural Networks. 
The neural networks were trained on data from whole-exome and RNA-sequencing data from 70 individuals with metastatic cancer with at least one human leukocyte antigen (HLA) class I-restricted epitope. The model requires next-generation sequencing data and utilizes the stacking ensemble method by calculating scores from state-of-the-art models (MHCFlurry1.6, NetMHCstabpan-1.0, and IEDB.) The model’s architecture includes an FFNN and an RNN with LSTM layers with memory to analyze both sequential and non-sequential data. Both model’s results are aggregated to produce predictions. Using this model, personalized cancer vaccines can be produced with improved results (0.9166 AUC, recall = 91.67%,).


Acknowledgements: I would like to thank Dr. Ashley Posey at the McCallie School for her mentorship and wisdom throughout this project. Additionally, Dr. Giovanni Parmigiani, Mrs. Ezhilvadivu Palaniyappan, Mrs. Neelima Maddy, and Ms. Jenna Landy are thanked for providing feedback on my project and knowledge in machine learning and artificial intelligence.


April 2024 Publication in the Tennessee Junior Academy of Science: https://docs.google.com/document/d/1wlOEumR5EUMQlySvfDmWygOdSDg6HwUJy7v4OngBils/edit?tab=t.0
2024 Tennessee Junior Academy of Science Conference Slides: https://docs.google.com/presentation/d/1Q_NVlLSbzqD9J6cZFRc2SAKdszLJquZbn-tSEozpdW8/edit#slide=id.p
International Science and Engineering Fair (ISEF) Regionals Poster: 


Accolades:
- 1st Place in Translational Medical Sciences (TMED) at Chattanooga Regional Science and Engineering Fair
- Regeneron Biomedical Science Award (1st/112, $375)
- Runner-Up at Tennessee Junior Academy of Science 2024 Conference ($1,200)
- American Junior Academy of Science 2025 Selected Project
- American Academy of the Advancement of Science Special Guest Attendee
