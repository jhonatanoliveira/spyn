import dataset

train, valid, test = dataset.load_train_val_test_csvs("bnetflix")
freqs, features = dataset.data_2_freqs(train)
print(train.shape)
print(len(features))