# points

## Overview

Float-point vectors with payload.

### Available Operations

* [clear_payload](#clear_payload) - Clear payload
* [count_points](#count_points) - Count points
* [delete_payload](#delete_payload) - Delete payload
* [delete_points](#delete_points) - Delete points
* [get_point](#get_point) - Get point
* [get_points](#get_points) - Get points
* [overwrite_payload](#overwrite_payload) - Overwrite payload
* [recommend_batch_points](#recommend_batch_points) - Recommend batch points
* [recommend_points](#recommend_points) - Recommend points
* [scroll_points](#scroll_points) - Scroll points
* [search_batch_points](#search_batch_points) - Search batch points
* [search_points](#search_points) - Search points
* [set_payload](#set_payload) - Set payload
* [upsert_points](#upsert_points) - Upsert points

## clear_payload

Remove all payload for specified points

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.ClearPayloadRequest(
    request_body=shared.FilterSelector(
        filter=shared.Filter(
            must=[
                shared.FieldCondition(
                    geo_bounding_box='est',
                    geo_radius='laborum',
                    key='dolores',
                    match=shared.MatchText(
                        text='explicabo',
                    ),
                    range='enim',
                    values_count='nemo',
                ),
            ],
            must_not=[
                shared.IsNullCondition(
                    is_null=shared.PayloadField(
                        key='accusantium',
                    ),
                ),
                shared.IsNullCondition(
                    is_null=shared.PayloadField(
                        key='culpa',
                    ),
                ),
            ],
            should=[
                shared.Filter(),
                shared.FieldCondition(
                    geo_bounding_box='dolorem',
                    geo_radius='consequuntur',
                    key='repellat',
                    match='occaecati',
                    range=shared.Range(
                        gt=4143.69,
                        gte=4663.11,
                        lt=4746.97,
                        lte=2444.25,
                    ),
                    values_count='quia',
                ),
                shared.IsEmptyCondition(
                    is_empty=shared.PayloadField(
                        key='vitae',
                    ),
                ),
                shared.HasIDCondition(
                    has_id=[
                        138183,
                        '3f5ad019-da1f-4fe7-8f09-7b0074f15471',
                        '5e6e13b9-9d48-48e1-a91e-450ad2abd442',
                    ],
                ),
            ],
        ),
    ),
    collection_name='aliquid',
    ordering=shared.WriteOrderingEnum.MEDIUM,
    wait=False,
)

res = s.points.clear_payload(req)

if res.clear_payload_200_application_json_object is not None:
    # handle response
```

## count_points

Count points which matches given filtering condition

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.CountPointsRequest(
    count_request=shared.CountRequest(
        exact=False,
        filter='perferendis',
    ),
    collection_name='magni',
)

res = s.points.count_points(req)

if res.count_points_200_application_json_object is not None:
    # handle response
```

## delete_payload

Delete specified key payload for points

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.DeletePayloadRequest(
    delete_payload=shared.DeletePayload(
        filter='ipsam',
        keys=[
            'fugit',
        ],
        points=[
            '4bb4f63c-969e-49a3-afa7-7dfb14cd66ae',
            581273,
            881736,
        ],
    ),
    collection_name='delectus',
    ordering=shared.WriteOrderingEnum.STRONG,
    wait=False,
)

res = s.points.delete_payload(req)

if res.delete_payload_200_application_json_object is not None:
    # handle response
```

## delete_points

Delete points

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.DeletePointsRequest(
    request_body=shared.FilterSelector(
        filter=shared.Filter(
            must=[
                shared.HasIDCondition(
                    has_id=[
                        'f3a66997-074b-4a44-a9b6-e2141959890a',
                        'a563e251-6fe4-4c8b-b11e-5b7fd2ed0289',
                        123820,
                    ],
                ),
                shared.HasIDCondition(
                    has_id=[
                        'c692601f-b576-4b0d-9f0d-30c5fbb25870',
                        199996,
                        18521,
                        793698,
                    ],
                ),
                shared.IsNullCondition(
                    is_null=shared.PayloadField(
                        key='dolor',
                    ),
                ),
            ],
            must_not=[
                shared.IsEmptyCondition(
                    is_empty=shared.PayloadField(
                        key='hic',
                    ),
                ),
                shared.Filter(),
                shared.HasIDCondition(
                    has_id=[
                        '0c28909b-3fe4-49a8-99cb-f48633323f9b',
                        490459,
                        '3a410067-4ebf-4692-80d1-ba77a89ebf73',
                    ],
                ),
                shared.IsNullCondition(
                    is_null=shared.PayloadField(
                        key='id',
                    ),
                ),
            ],
            should=[
                shared.IsEmptyCondition(
                    is_empty=shared.PayloadField(
                        key='aspernatur',
                    ),
                ),
                shared.FieldCondition(
                    geo_bounding_box=shared.GeoBoundingBox(
                        bottom_right=shared.GeoPoint(
                            lat=7583.79,
                            lon=8815.86,
                        ),
                        top_left=shared.GeoPoint(
                            lat=3200.17,
                            lon=9044.25,
                        ),
                    ),
                    geo_radius=shared.GeoRadius(
                        center=shared.GeoPoint(
                            lat=6457.85,
                            lon=5883.17,
                        ),
                        radius=3246.83,
                    ),
                    key='repellendus',
                    match='similique',
                    range=shared.Range(
                        gt=8726.51,
                        gte=3118.6,
                        lt=2735.42,
                        lte=4254.51,
                    ),
                    values_count='officiis',
                ),
                shared.FieldCondition(
                    geo_bounding_box='a',
                    geo_radius=shared.GeoRadius(
                        center=shared.GeoPoint(
                            lat=6874.88,
                            lon=4834.09,
                        ),
                        radius=2155.07,
                    ),
                    key='quisquam',
                    match='amet',
                    range='accusamus',
                    values_count=shared.ValuesCount(
                        gt=313692,
                        gte=213312,
                        lt=957451,
                        lte=518201,
                    ),
                ),
                shared.IsNullCondition(
                    is_null=shared.PayloadField(
                        key='sit',
                    ),
                ),
            ],
        ),
    ),
    collection_name='expedita',
    ordering=shared.WriteOrderingEnum.WEAK,
    wait=False,
)

res = s.points.delete_points(req)

if res.delete_points_200_application_json_object is not None:
    # handle response
```

## get_point

Retrieve full information of single point by id

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.GetPointRequest(
    collection_name='sed',
    consistency=730442,
    id=646265,
)

res = s.points.get_point(req)

if res.get_point_200_application_json_object is not None:
    # handle response
```

## get_points

Retrieve multiple points by specified IDs

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.GetPointsRequest(
    point_request=shared.PointRequest(
        ids=[
            277628,
            586784,
        ],
        with_payload='pariatur',
        with_vector=[
            'laborum',
        ],
    ),
    collection_name='totam',
    consistency=132068,
)

res = s.points.get_points(req)

if res.get_points_200_application_json_object is not None:
    # handle response
```

## overwrite_payload

Replace full payload of points with new one

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.OverwritePayloadRequest(
    set_payload=shared.SetPayload(
        filter=shared.Filter(
            must=[
                shared.HasIDCondition(
                    has_id=[
                        565421,
                        '2322715b-f0cb-4b1e-b1b8-b90f3443a110',
                    ],
                ),
                shared.IsNullCondition(
                    is_null=shared.PayloadField(
                        key='itaque',
                    ),
                ),
                shared.FieldCondition(
                    geo_bounding_box='repellendus',
                    geo_radius='doloribus',
                    key='ut',
                    match='cupiditate',
                    range=shared.Range(
                        gt=639.55,
                        gte=5123.93,
                        lt=4856.28,
                        lte=5804.47,
                    ),
                    values_count='quisquam',
                ),
            ],
            must_not=[
                shared.HasIDCondition(
                    has_id=[
                        961571,
                        231701,
                    ],
                ),
                shared.Filter(),
                shared.Filter(),
                shared.IsNullCondition(
                    is_null=shared.PayloadField(
                        key='hic',
                    ),
                ),
            ],
            should=[
                shared.HasIDCondition(
                    has_id=[
                        'bd74dd39-c0f5-4d2c-bf7c-70a45626d436',
                        '13f16d9f-5fce-46c5-9614-6c3e250fb008',
                    ],
                ),
                shared.HasIDCondition(
                    has_id=[
                        882860,
                        250622,
                    ],
                ),
                shared.FieldCondition(
                    geo_bounding_box='laborum',
                    geo_radius='velit',
                    key='eum',
                    match=shared.MatchAny(
                        any=[
                            860552,
                            379034,
                            727044,
                            96549,
                        ],
                    ),
                    range=shared.Range(
                        gt=2561.39,
                        gte=1314.82,
                        lt=5919.35,
                        lte=553.74,
                    ),
                    values_count=shared.ValuesCount(
                        gt=301598,
                        gte=487935,
                        lt=262118,
                        lte=458515,
                    ),
                ),
            ],
        ),
        payload={
            "rem": 'fuga',
            "reprehenderit": 'quidem',
        },
        points=[
            433439,
            826871,
            509342,
            '10ab3cdc-a425-4190-8e52-3c7e0bc7178e',
        ],
    ),
    collection_name='aliquam',
    ordering=shared.WriteOrderingEnum.MEDIUM,
    wait=False,
)

res = s.points.overwrite_payload(req)

if res.overwrite_payload_200_application_json_object is not None:
    # handle response
```

## recommend_batch_points

Look for the points which are closer to stored positive examples and at the same time further to negative examples.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.RecommendBatchPointsRequest(
    recommend_request_batch=shared.RecommendRequestBatch(
        searches=[
            shared.RecommendRequest(
                filter=shared.Filter(
                    must=[
                        shared.FieldCondition(
                            geo_bounding_box='molestiae',
                            geo_radius=shared.GeoRadius(
                                center=shared.GeoPoint(
                                    lat=7836.48,
                                    lon=4304.02,
                                ),
                                radius=5564.29,
                            ),
                            key='praesentium',
                            match=shared.MatchText(
                                text='fugit',
                            ),
                            range='mollitia',
                            values_count=shared.ValuesCount(
                                gt=539224,
                                gte=128860,
                                lt=325685,
                                lte=392676,
                            ),
                        ),
                        shared.FieldCondition(
                            geo_bounding_box='consequuntur',
                            geo_radius=shared.GeoRadius(
                                center=shared.GeoPoint(
                                    lat=1294.12,
                                    lon=9039.84,
                                ),
                                radius=5789.22,
                            ),
                            key='atque',
                            match=shared.MatchText(
                                text='eveniet',
                            ),
                            range='veritatis',
                            values_count=shared.ValuesCount(
                                gt=800379,
                                gte=724168,
                                lt=877131,
                                lte=399025,
                            ),
                        ),
                        shared.FieldCondition(
                            geo_bounding_box='vel',
                            geo_radius='molestiae',
                            key='rerum',
                            match='minima',
                            range='eligendi',
                            values_count=shared.ValuesCount(
                                gt=636061,
                                gte=731398,
                                lt=240020,
                                lte=766964,
                            ),
                        ),
                        shared.FieldCondition(
                            geo_bounding_box=shared.GeoBoundingBox(
                                bottom_right=shared.GeoPoint(
                                    lat=7963.92,
                                    lon=3082.86,
                                ),
                                top_left=shared.GeoPoint(
                                    lat=9591.67,
                                    lon=2328.65,
                                ),
                            ),
                            geo_radius=shared.GeoRadius(
                                center=shared.GeoPoint(
                                    lat=5034.27,
                                    lon=5909.84,
                                ),
                                radius=9537.22,
                            ),
                            key='nulla',
                            match='esse',
                            range=shared.Range(
                                gt=9518.75,
                                gte=6216.79,
                                lt=5757.51,
                                lte=8630.23,
                            ),
                            values_count='quia',
                        ),
                    ],
                    must_not=[
                        shared.Filter(),
                        shared.Filter(),
                        shared.FieldCondition(
                            geo_bounding_box=shared.GeoBoundingBox(
                                bottom_right=shared.GeoPoint(
                                    lat=944.58,
                                    lon=6288.99,
                                ),
                                top_left=shared.GeoPoint(
                                    lat=6336.08,
                                    lon=3984.34,
                                ),
                            ),
                            geo_radius='quae',
                            key='earum',
                            match=shared.MatchText(
                                text='eius',
                            ),
                            range='illum',
                            values_count='accusantium',
                        ),
                        shared.IsEmptyCondition(
                            is_empty=shared.PayloadField(
                                key='sapiente',
                            ),
                        ),
                    ],
                    should=[
                        shared.IsEmptyCondition(
                            is_empty=shared.PayloadField(
                                key='reprehenderit',
                            ),
                        ),
                    ],
                ),
                limit=356707,
                lookup_from=shared.LookupLocation(
                    collection='aut',
                    vector='voluptatum',
                ),
                negative=[
                    '68ea19f1-d170-4513-b9d0-8086a1840394',
                ],
                offset=771089,
                params=shared.SearchParams(
                    exact=False,
                    hnsw_ef=376226,
                    quantization=shared.QuantizationSearchParams(
                        ignore=False,
                        rescore=False,
                    ),
                ),
                positive=[
                    981640,
                    '3f5f0642-dac7-4af5-95cc-413aa63aae8d',
                ],
                score_threshold=4240.89,
                using='quos',
                with_payload=False,
                with_vector='facilis',
            ),
            shared.RecommendRequest(
                filter='commodi',
                limit=447144,
                lookup_from=shared.LookupLocation(
                    collection='reiciendis',
                    vector='assumenda',
                ),
                negative=[
                    '60b375ed-4f6f-4bee-81f3-3317fe35b60e',
                    '1ea42655-5ba3-4c28-b44e-d53b88f3a8d8',
                ],
                offset=940210,
                params=shared.SearchParams(
                    exact=False,
                    hnsw_ef=750765,
                    quantization=shared.QuantizationSearchParams(
                        ignore=False,
                        rescore=False,
                    ),
                ),
                positive=[
                    967966,
                    994401,
                    '7b194a27-6b26-4916-be1f-08f4294e3698',
                ],
                score_threshold=9757.52,
                using='tempora',
                with_payload=shared.PayloadSelectorInclude(
                    include=[
                        'non',
                    ],
                ),
                with_vector='praesentium',
            ),
            shared.RecommendRequest(
                filter='quaerat',
                limit=277773,
                lookup_from=shared.LookupLocation(
                    collection='debitis',
                    vector='rem',
                ),
                negative=[
                    'a55efd20-e457-4e18-98b6-a89fbe3a5aa8',
                ],
                offset=879235,
                params=shared.SearchParams(
                    exact=False,
                    hnsw_ef=543678,
                    quantization=shared.QuantizationSearchParams(
                        ignore=False,
                        rescore=False,
                    ),
                ),
                positive=[
                    '0ab40750-88e5-4186-a065-e904f3b1194b',
                    'abf603a7-9f9d-4fe0-ab7d-a8a50ce187f8',
                ],
                score_threshold=3831.03,
                using='maxime',
                with_payload=[
                    'assumenda',
                ],
                with_vector=[
                    'officiis',
                    'officiis',
                    'accusamus',
                ],
            ),
        ],
    ),
    collection_name='natus',
    consistency=133461,
)

res = s.points.recommend_batch_points(req)

if res.recommend_batch_points_200_application_json_object is not None:
    # handle response
```

## recommend_points

Look for the points which are closer to stored positive examples and at the same time further to negative examples.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.RecommendPointsRequest(
    recommend_request=shared.RecommendRequest(
        filter=shared.Filter(
            must=[
                shared.IsNullCondition(
                    is_null=shared.PayloadField(
                        key='at',
                    ),
                ),
                shared.HasIDCondition(
                    has_id=[
                        922348,
                        '81ead4f0-e101-4256-bf94-e29e973e922a',
                        440264,
                    ],
                ),
                shared.HasIDCondition(
                    has_id=[
                        696463,
                    ],
                ),
                shared.Filter(),
            ],
            must_not=[
                shared.Filter(),
            ],
            should=[
                shared.IsNullCondition(
                    is_null=shared.PayloadField(
                        key='ipsa',
                    ),
                ),
            ],
        ),
        limit=517612,
        lookup_from=shared.LookupLocation(
            collection='molestiae',
            vector='eveniet',
        ),
        negative=[
            '6e3ab884-5f05-497a-a0ff-2a54a31e9476',
        ],
        offset=284000,
        params='adipisci',
        positive=[
            '65e7956f-9251-4a5a-9da6-60ff57bfaad4',
            '9efc1b45-12c1-4032-a48d-c2f615199ebf',
            '0e9fe6c6-32ca-43ae-9011-7996312fde04',
            473190,
        ],
        score_threshold=1158.34,
        using='esse',
        with_payload='maiores',
        with_vector='vel',
    ),
    collection_name='architecto',
    consistency=shared.ReadConsistencyTypeEnum.MAJORITY,
)

res = s.points.recommend_points(req)

if res.recommend_points_200_application_json_object is not None:
    # handle response
```

## scroll_points

Scroll request - paginate over all points which matches given filtering condition

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.ScrollPointsRequest(
    scroll_request=shared.ScrollRequest(
        filter=shared.Filter(
            must=[
                shared.IsEmptyCondition(
                    is_empty=shared.PayloadField(
                        key='esse',
                    ),
                ),
                shared.IsNullCondition(
                    is_null=shared.PayloadField(
                        key='consectetur',
                    ),
                ),
            ],
            must_not=[
                shared.FieldCondition(
                    geo_bounding_box='sunt',
                    geo_radius=shared.GeoRadius(
                        center=shared.GeoPoint(
                            lat=8567.56,
                            lon=7137.67,
                        ),
                        radius=3996.67,
                    ),
                    key='officia',
                    match=shared.MatchText(
                        text='perferendis',
                    ),
                    range=shared.Range(
                        gt=3747.53,
                        gte=6145.28,
                        lt=6616.07,
                        lte=700.42,
                    ),
                    values_count='possimus',
                ),
                shared.Filter(),
            ],
            should=[
                shared.HasIDCondition(
                    has_id=[
                        536923,
                        110477,
                        '6c645b08-b618-491b-aa0f-e1ade008e6f8',
                    ],
                ),
                shared.HasIDCondition(
                    has_id=[
                        '350d8cdb-5a34-4181-8301-0421813d5208',
                        'ce7e253b-6684-451c-ac6e-205e16deab3f',
                    ],
                ),
                shared.Filter(),
            ],
        ),
        limit=759283,
        offset='nemo',
        with_payload=[
            'voluptas',
            'numquam',
            'nemo',
        ],
        with_vector=[
            'aspernatur',
            'ducimus',
        ],
    ),
    collection_name='nesciunt',
    consistency=shared.ReadConsistencyTypeEnum.QUORUM,
)

res = s.points.scroll_points(req)

if res.scroll_points_200_application_json_object is not None:
    # handle response
```

## search_batch_points

Retrieve by batch the closest points based on vector similarity and given filtering conditions

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.SearchBatchPointsRequest(
    search_request_batch=shared.SearchRequestBatch(
        searches=[
            shared.SearchRequest(
                filter=shared.Filter(
                    must=[
                        shared.Filter(),
                        shared.FieldCondition(
                            geo_bounding_box=shared.GeoBoundingBox(
                                bottom_right=shared.GeoPoint(
                                    lat=1598.45,
                                    lon=2330.78,
                                ),
                                top_left=shared.GeoPoint(
                                    lat=468.06,
                                    lon=5854.32,
                                ),
                            ),
                            geo_radius='soluta',
                            key='alias',
                            match='eos',
                            range='iste',
                            values_count=shared.ValuesCount(
                                gt=81369,
                                gte=686362,
                                lt=881897,
                                lte=976802,
                            ),
                        ),
                        shared.HasIDCondition(
                            has_id=[
                                '58c4d86e-68e4-4be0-9601-3f59da757a59',
                                'cfef66ef-1caa-4338-bc2b-eb477373c8d7',
                                974990,
                            ],
                        ),
                    ],
                    must_not=[
                        shared.IsEmptyCondition(
                            is_empty=shared.PayloadField(
                                key='quibusdam',
                            ),
                        ),
                        shared.FieldCondition(
                            geo_bounding_box='libero',
                            geo_radius=shared.GeoRadius(
                                center=shared.GeoPoint(
                                    lat=9754.25,
                                    lon=1563.83,
                                ),
                                radius=7820.9,
                            ),
                            key='aliquam',
                            match=shared.MatchValue(
                                value='vel',
                            ),
                            range=shared.Range(
                                gt=1076.17,
                                gte=8777.51,
                                lt=5682.18,
                                lte=4319.94,
                            ),
                            values_count=shared.ValuesCount(
                                gt=284086,
                                gte=596433,
                                lt=935302,
                                lte=117525,
                            ),
                        ),
                    ],
                    should=[
                        shared.Filter(),
                        shared.HasIDCondition(
                            has_id=[
                                391797,
                                '3a437000-ae6b-46bc-9b8f-759eac55a974',
                                874400,
                                112427,
                            ],
                        ),
                        shared.FieldCondition(
                            geo_bounding_box=shared.GeoBoundingBox(
                                bottom_right=shared.GeoPoint(
                                    lat=3220.17,
                                    lon=1830.33,
                                ),
                                top_left=shared.GeoPoint(
                                    lat=6113.28,
                                    lon=4030.26,
                                ),
                            ),
                            geo_radius=shared.GeoRadius(
                                center=shared.GeoPoint(
                                    lat=7452.33,
                                    lon=7262.27,
                                ),
                                radius=5269.07,
                            ),
                            key='dolorum',
                            match=shared.MatchValue(
                                value='magni',
                            ),
                            range=shared.Range(
                                gt=644.35,
                                gte=635.53,
                                lt=2643.33,
                                lte=2082.53,
                            ),
                            values_count=shared.ValuesCount(
                                gt=932394,
                                gte=88248,
                                lt=215398,
                                lte=602229,
                            ),
                        ),
                        shared.Filter(),
                    ],
                ),
                limit=714376,
                offset=802894,
                params=shared.SearchParams(
                    exact=False,
                    hnsw_ef=159146,
                    quantization=shared.QuantizationSearchParams(
                        ignore=False,
                        rescore=False,
                    ),
                ),
                score_threshold=6057.12,
                vector=shared.NamedVector(
                    name='Alberta Rempel',
                    vector=[
                        8119.39,
                        257.56,
                        4793.85,
                    ],
                ),
                with_payload=shared.PayloadSelectorInclude(
                    include=[
                        'totam',
                    ],
                ),
                with_vector=[
                    'voluptatem',
                    'autem',
                    'esse',
                ],
            ),
            shared.SearchRequest(
                filter=shared.Filter(
                    must=[
                        shared.FieldCondition(
                            geo_bounding_box='facere',
                            geo_radius='molestiae',
                            key='provident',
                            match='necessitatibus',
                            range='sint',
                            values_count=shared.ValuesCount(
                                gt=421819,
                                gte=373511,
                                lt=702952,
                                lte=515638,
                            ),
                        ),
                        shared.IsEmptyCondition(
                            is_empty=shared.PayloadField(
                                key='officiis',
                            ),
                        ),
                        shared.Filter(),
                        shared.HasIDCondition(
                            has_id=[
                                156653,
                                'ae0be2d7-8225-49e3-aa4b-5197f92443da',
                                760744,
                                '52b895c5-37c6-4454-afb0-b34896c3ca5a',
                            ],
                        ),
                    ],
                    must_not=[
                        shared.Filter(),
                        shared.HasIDCondition(
                            has_id=[
                                997437,
                                '57075779-2917-47de-ac64-6ecb573409e3',
                                'b1e5a2b1-2eb0-47f1-96db-99545fc95fa8',
                                '970e189d-bb30-4fcb-b3ea-055b197cd44e',
                            ],
                        ),
                        shared.FieldCondition(
                            geo_bounding_box='veniam',
                            geo_radius=shared.GeoRadius(
                                center=shared.GeoPoint(
                                    lat=8138.8,
                                    lon=5129.05,
                                ),
                                radius=1403.84,
                            ),
                            key='pariatur',
                            match=shared.MatchText(
                                text='ab',
                            ),
                            range=shared.Range(
                                gt=7057.1,
                                gte=7310.65,
                                lt=3952.33,
                                lte=9775.18,
                            ),
                            values_count=shared.ValuesCount(
                                gt=503748,
                                gte=718627,
                                lt=392430,
                                lte=335977,
                            ),
                        ),
                        shared.IsEmptyCondition(
                            is_empty=shared.PayloadField(
                                key='libero',
                            ),
                        ),
                    ],
                    should=[
                        shared.Filter(),
                        shared.HasIDCondition(
                            has_id=[
                                973819,
                            ],
                        ),
                        shared.Filter(),
                        shared.FieldCondition(
                            geo_bounding_box='labore',
                            geo_radius='eos',
                            key='reprehenderit',
                            match=shared.MatchValue(
                                value=664965,
                            ),
                            range='eligendi',
                            values_count='unde',
                        ),
                    ],
                ),
                limit=889448,
                offset=495617,
                params=shared.SearchParams(
                    exact=False,
                    hnsw_ef=118041,
                    quantization='porro',
                ),
                score_threshold=1114.96,
                vector=[
                    8541.15,
                    3223.33,
                ],
                with_payload=False,
                with_vector='iusto',
            ),
        ],
    ),
    collection_name='dignissimos',
    consistency=shared.ReadConsistencyTypeEnum.MAJORITY,
)

res = s.points.search_batch_points(req)

if res.search_batch_points_200_application_json_object is not None:
    # handle response
```

## search_points

Retrieve closest points based on vector similarity and given filtering conditions

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.SearchPointsRequest(
    search_request=shared.SearchRequest(
        filter=shared.Filter(
            must=[
                shared.Filter(),
                shared.Filter(),
            ],
            must_not=[
                shared.IsEmptyCondition(
                    is_empty=shared.PayloadField(
                        key='eos',
                    ),
                ),
                shared.Filter(),
                shared.Filter(),
            ],
            should=[
                shared.IsNullCondition(
                    is_null=shared.PayloadField(
                        key='nemo',
                    ),
                ),
                shared.Filter(),
            ],
        ),
        limit=789770,
        offset=197259,
        params=shared.SearchParams(
            exact=False,
            hnsw_ef=534908,
            quantization=shared.QuantizationSearchParams(
                ignore=False,
                rescore=False,
            ),
        ),
        score_threshold=2902.48,
        vector=shared.NamedVector(
            name='Alexandra McLaughlin',
            vector=[
                8052.64,
            ],
        ),
        with_payload=shared.PayloadSelectorExclude(
            exclude=[
                'provident',
                'repudiandae',
                'rerum',
            ],
        ),
        with_vector=False,
    ),
    collection_name='vero',
    consistency=shared.ReadConsistencyTypeEnum.ALL,
)

res = s.points.search_points(req)

if res.search_points_200_application_json_object is not None:
    # handle response
```

## set_payload

Set payload values for points

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.SetPayloadRequest(
    set_payload=shared.SetPayload(
        filter=shared.Filter(
            must=[
                shared.IsNullCondition(
                    is_null=shared.PayloadField(
                        key='impedit',
                    ),
                ),
            ],
            must_not=[
                shared.FieldCondition(
                    geo_bounding_box=shared.GeoBoundingBox(
                        bottom_right=shared.GeoPoint(
                            lat=3228.29,
                            lon=609.95,
                        ),
                        top_left=shared.GeoPoint(
                            lat=2295.67,
                            lon=8493.2,
                        ),
                    ),
                    geo_radius='quidem',
                    key='cum',
                    match=shared.MatchValue(
                        value='laudantium',
                    ),
                    range=shared.Range(
                        gt=9384.12,
                        gte=4797.07,
                        lt=2286.46,
                        lte=5879.67,
                    ),
                    values_count='necessitatibus',
                ),
                shared.IsNullCondition(
                    is_null=shared.PayloadField(
                        key='repudiandae',
                    ),
                ),
            ],
            should=[
                shared.IsEmptyCondition(
                    is_empty=shared.PayloadField(
                        key='molestiae',
                    ),
                ),
            ],
        ),
        payload={
            "facilis": 'corrupti',
            "aperiam": 'sint',
            "accusamus": 'eos',
            "totam": 'dicta',
        },
        points=[
            224413,
        ],
    ),
    collection_name='sunt',
    ordering=shared.WriteOrderingEnum.STRONG,
    wait=False,
)

res = s.points.set_payload(req)

if res.set_payload_200_application_json_object is not None:
    # handle response
```

## upsert_points

Perform insert + updates on points. If point with given ID already exists - it will be overwritten.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()

req = operations.UpsertPointsRequest(
    request_body=shared.PointsBatch(
        batch=shared.Batch(
            ids=[
                '1d4c700b-607f-43c9-bc73-b9da3f2ceda7',
                '23f22574-11fa-4f4b-b544-e472e802857a',
                727544,
            ],
            payloads=[
                {
                    "eum": 'nesciunt',
                    "mollitia": 'dignissimos',
                },
                'nostrum',
            ],
            vectors=[
                [
                    662.07,
                    2656.32,
                    138.65,
                    135.08,
                ],
                [
                    4837.53,
                    4137.58,
                    2561.14,
                    6770.45,
                ],
            ],
        ),
    ),
    collection_name='possimus',
    ordering=shared.WriteOrderingEnum.MEDIUM,
    wait=False,
)

res = s.points.upsert_points(req)

if res.upsert_points_200_application_json_object is not None:
    # handle response
```
