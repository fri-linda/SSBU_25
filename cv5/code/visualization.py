from data_handling_done import Dataset

if __name__ == "__main__":
    dataset_std = Dataset()
    dataset_norm = Dataset()

    # split and scale data
    X_train_s, X_test_s, y_train_s, _ = dataset_std.split_data()
    X_train_n, X_test_n, y_train_n, _ = dataset_std.split_data()

    # standardization
    X_train_standard, _ = dataset_std.scale_data(X_train_s, X_test_s, scale_type='standard')
    dataset_std.plot_all_features_before_after_scaling(X_train_s, X_train_standard, scale_type='Standardization')
    dataset_std.plot_feature_before_after_scaling(X_train_s, X_train_standard, feature_name='mean area')
    dataset_std.plot_box_plots(scaled_data=X_train_standard, target=y_train_s)

    # normalization
    X_train_norm, _ = dataset_norm.scale_data(X_train_n, X_test_n, scale_type='normalize')
    dataset_norm.plot_all_features_before_after_scaling(X_train_n, X_train_norm, scale_type='Normalization')
    dataset_norm.plot_feature_before_after_scaling(X_train_n, X_train_norm, feature_name='mean area')
    dataset_norm.plot_box_plots(scaled_data=X_train_norm, target=y_train_n)