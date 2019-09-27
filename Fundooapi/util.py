class GetUser:
    user_list = []

    def add_list(self, username):
        self.user_list.append(username)
        return True

    def get_list(self):
        return self.user_list
