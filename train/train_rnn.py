import torch
from torch.utils.data import DataLoader, TensorDataset
from models.rnn_model import RNN
from utils.data_preprocessing import preprocess_data, split_data

def train_rnn(X_train, y_train, X_val, y_val):
    batch_size = 100
    input_size = X_train.shape[1]
    hidden_size = 32
    num_layers = 2
    num_classes = 1

    model = RNN(input_size, hidden_size, num_layers, num_classes)
    criterion = torch.nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    train_dataset = TensorDataset(torch.Tensor(X_train), torch.Tensor(y_train))
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    # Training loop here...
    for epoch in range(5):  # Adjust number of epochs as needed
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

