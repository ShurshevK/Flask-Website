# Create resource managers and endpoints

from flask_rest_jsonapi import Api, ResourceDetail, ResourceList

class ArtistMany(ResourceList):
    schema = ArtistSchema
    data_layer = {'session': db.session,
                  'model': Artist}

class ArtistOne(ResourceDetail):
    schema = ArtistSchema
    data_layer = {'session': db.session,
                  'model': Artist}

api = Api(app)
api.route(ArtistMany, 'artist_many', '/artists')
api.route(ArtistOne, 'artist_one', '/artists/<int:id>')

# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)