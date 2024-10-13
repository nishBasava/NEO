import torch
from torch.utils.data import DataLoader, TensorDataset
from models.ann_model import ANN_predictions
from utils.data_preprocessing import preprocess_data, split_data

def train_ann(X_train, y_train, X_val, y_val):
    batch_size = 100
    model = ANN_predictions()
    criterion = torch.nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    train_dataset = TensorDataset(torch.Tensor(X_train), torch.Tensor(y_train))
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    # Training loop here...
    for epoch in range(100):  # Adjust number of epochs as needed
        model.train()
        for batch in train_loader:
            inputs, labels = batch
            outputs = model(inputs)
            loss = criterion(outputs, labels.unsqueeze(1))

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # Add validation and print the loss if needed
        print(f"Epoch {epoch}, Loss: {loss.item()}")

