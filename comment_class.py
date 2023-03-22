class Comment:

    def __init__ (self, user_id, comment_text, likes, dislikes, owner):
        self.user_id = user_id
        self.comment_text = comment_text
        self.likes = likes
        self.dislikes = dislikes
        self.owner = owner

    # def showUser(self):
    #     if self.min_in_Oven > 10:
    #         if self.min_in_Oven > 30:
    #             print("Your cookie is burnt, bro.")
    #         else:
    #             print("Cookie is cooked, fully.")
    #     else:
    #         print("Cookie isn't quite done yet.")
    #     return self