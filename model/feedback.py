class Feedback:

    def __init__(self, impression, score, comment):
        self.__impression = impression
        self.__score = score
        self.__comment = comment

    @property
    def impression(self):
        return self.__impression

    @impression.setter
    def impression(self, impression):
        self.__impression = impression

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment):
        self.__comment = comment


    def __str__(self):
        return f'Общее впечатление: {self.__impression}\n' \
               f'Оценка: {self.__score}\n' \
               f'Комментарий: {self.__comment}'