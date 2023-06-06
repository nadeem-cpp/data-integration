import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class DataHandler:
    def __init__(self, data_files: list, separator: str = ","):
        self.__data_files = data_files
        self.__sep = separator
        self.__data_list = []
        self.__file_names = []
        for data_file in data_files:
            self.__file_names.append(data_file.filename)
            data = pd.read_csv(data_file, sep=self.__sep)
            self.__data_list.append(data)

    def get_similar_titles(self):
        """return a list of tuples where each tuple show column names that are going to get merged"""
        columns = []
        for data in self.__data_list:
            columns.append(data.columns.tolist())

        main_remove = []
        similar = []
        # TODO 1 create a tuples of columns with same names or similar names like name, sure name
        for i in range(1, len(columns)):
            for j, name1 in enumerate(columns[0]):
                for k, name2 in enumerate(columns[i]):
                    if name1 == name2:
                        similar.append({self.__file_names[0]:name1, self.__file_names[i]: name2})
                        # similar.append((name1, name2))
                        main_remove.append(name1)
                        del columns[i][k]
                    elif name1 in name2:
                        similar.append({self.__file_names[0]:name1, self.__file_names[i]: name2})
                        # similar.append((name1, name2))
                        main_remove.append(name1)
                        del columns[i][k]

        # remove matched data from main_dataset to avoid extra computation
        for name in main_remove:
            columns[0].remove(name)

        # columns_temp = self.__cosine_similarity(columns)
        #
        # if len(columns_temp) is not 0:
        #     similar.append(columns_temp)

        return similar

    def __cosine_similarity(self, unmatched: list):
        # TODO 2  apply cosine similarity on remaining columns
        # getting a portion of dataset whose columns names are different
        dataframes = []
        for i, unmatch in enumerate(unmatched):
            dataframes.append(self.__data_list[i].loc[:, unmatch])

        vectorizer = TfidfVectorizer()
        features = []
        # transform datasets into scaled valued understandable by model
        for df in dataframes:
            features.append(vectorizer.fit_transform(df))

        # cosine similarity
        # calculate cosine similarity between datasets and append them is a list
        cosine_similarity_matrix = []
        for i in range(len(features)):
            for j in range(i + 1, len(features)):
                similarity_matrix_temp = cosine_similarity(features[i], features[j])
                cosine_similarity_matrix.append(similarity_matrix_temp)

        threshold = 0.8
        similar_columns = []

        # find similarity with respect to threshold on each calculated similarity matrix
        for similarity_matrix in cosine_similarity_matrix:
            most_similar_indices = similarity_matrix.argmax(axis=1)
            for i, j in enumerate(most_similar_indices):
                similarity_score = similarity_matrix[i, j]
                if similarity_score > threshold:
                    similar_columns.append((dataframes[i].columns, dataframes[j].columns))

        return similar_columns

    def __data_cleaning(self):
        pass


# TODO 3 let user decide if we have choosed right columns for merge


