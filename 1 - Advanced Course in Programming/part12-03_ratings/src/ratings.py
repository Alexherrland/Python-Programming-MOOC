# TEE RATKAISUSI TÄHÄN:

def sort_by_ratings(items: list):
    def sort_rating(item: dict):
        return item["rating"]
    return sorted(items, key=sort_rating, reverse=True)
