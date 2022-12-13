import grpc

from . import cards_pb2
from . import cards_pb2_grpc

sample = [
    cards_pb2.CardResponse(card_id=1, card_name='Вино', brand='Apostrophe', type='Біле, Напівсухе',
                           percentages=13, picture_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNDaO2Vnm_tifcSQy_YQZw55sH-BV8kHW4YiWxI1X_3OmHHIUtYtHS5pSUbP8RpT0BpEM&usqp=CAU', likes=1, dislikes=0),
    cards_pb2.CardResponse(card_id=2, card_name='Вино', brand='Dog Smile', type='Біле, сухе',
                           percentages=12, picture_url='https://m.media-amazon.com/images/I/61BrYA2GgaL._SY550_.jpg', likes=0, dislikes=0),
    cards_pb2.CardResponse(card_id=3, card_name='Вино', brand='Apostrophe\" Chardonnay', type='Червоне, Сухе',
                           percentages=14, picture_url='https://5.imimg.com/data5/ANDROID/Default/2020/10/RS/SN/CW/98405810/img-20200822-wa0020-jpg-500x500.jpg', likes=0, dislikes=0),
    cards_pb2.CardResponse(card_id=4, card_name='Вино', brand='Acantus', type='Червоне, напівсухе',
                           percentages=13, picture_url='https://cgtwines.com/wp-content/uploads/2019/05/l-tbw-cherry.jpg', likes=0, dislikes=0),
    cards_pb2.CardResponse(card_id=5, card_name='Вино', brand='Botter', type='Червоне, напівсолодке',
                           percentages=12, picture_url='https://www.liz-palmer.com/wp-content/uploads/2021/05/1006238x.jpg', likes=0, dislikes=0),
    
]


class RecommendationService(cards_pb2_grpc.CardsServicer):
    def GetCard(self, request, context):
        card_id = request.card_id
        card = next(filter(lambda x: x.card_id == card_id, sample))
        if card:
            return card
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "Card not found")

    def ReactOnCard(self, request, context):
        card_id = request.card_id
        card = next(filter(lambda x: x.card_id == card_id, sample))
        if card:
            if request.is_like:
                card.likes += 1
            else:
                card.dislikes += 1
            return card
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "Card not found")
