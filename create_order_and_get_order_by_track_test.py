import data
import sender_stand_request


def test_create_order_and_get_order_by_track():
    response = sender_stand_request.post_new_order(data.order_body)

    assert response.status_code == 201

    json_response = response.json()
    track = json_response['track']

    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200
