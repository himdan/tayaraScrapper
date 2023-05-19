import json
from tayara_stats.models import RealEstate


def handle_log(ch, method, properties, body):
    print(" [x] Received %r" % body.decode('utf-8'))


def handle_insert_result(ch, method, properties, body: bytes):
    try:
        _payload = json.loads(body.decode('utf-8'))
        _metadata_payload = _payload.get('metadata')
        try:
            _real_estate = RealEstate.objects.get(reference=_payload.get('id'))
        except RealEstate.DoesNotExist:
            _real_estate = RealEstate.DoesNotExist
        _real_estate = RealEstate(
            reference=_payload.get('id'),
            title=_payload.get('title'),
            imgLoad=_payload.get('imgLoad'),
            description=_payload.get('description'),
            price=_payload.get('price'),
            phone=_payload.get('phone'),
            publishedOn=_metadata_payload.get('publishedOn'),
            isModified=_metadata_payload.get('isModified'),
            subCategory=_metadata_payload.get('subCategory'),
            isFeatured=_metadata_payload.get('isFeatured'),
            producttype=_metadata_payload.get('producttype'),
            images={"image": _payload.get('images')},
            pub_isApproved=_metadata_payload.get('publisher').get('isApproved'),
            pub_name=_metadata_payload.get('publisher').get('name'),
            pub_isShop=_metadata_payload.get('publisher').get('isShop'),
            pub_avatar=_metadata_payload.get('publisher').get('avatar'),
            loc_delegation=_payload.get('location').get('delegation'),
            loc_governorate=_payload.get('location').get('governorate'),

        ) if _real_estate is RealEstate.DoesNotExist else _real_estate
        _real_estate.reference = _payload.get('id')
        _real_estate.title = _payload.get('title')
        _real_estate.imgLoad = _payload.get('imgLoad')
        _real_estate.description = _payload.get('description')
        _real_estate.price = _payload.get('price')
        _real_estate.phone = _payload.get('phone')
        _real_estate.publishedOn = _metadata_payload.get('publishedOn')
        _real_estate.isModified = _metadata_payload.get('isModified')
        _real_estate.subCategory = _metadata_payload.get('subCategory')
        _real_estate.isFeatured = _metadata_payload.get('isFeatured')
        _real_estate.producttype = _metadata_payload.get('producttype')
        _real_estate.images = {"images": _payload.get('images')}
        _real_estate.pub_isApproved = _metadata_payload.get('publisher').get('isApproved')
        _real_estate.pub_name = _metadata_payload.get('publisher').get('name')
        _real_estate.pub_isShop = _metadata_payload.get('publisher').get('isShop')
        _real_estate.pub_avatar = _metadata_payload.get('publisher').get('avatar')
        _real_estate.loc_delegation = _payload.get('location').get('delegation')
        _real_estate.loc_governorate = _payload.get('location').get('governorate')
        _real_estate.save()
    except Exception as e:
        print(e)
