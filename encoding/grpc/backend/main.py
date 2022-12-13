from concurrent import futures
import grpc

import src.cards_pb2_grpc as cards_pb2_grpc
import src.cards as cards


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cards_pb2_grpc.add_CardsServicer_to_server(
        cards.RecommendationService(), server)
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
