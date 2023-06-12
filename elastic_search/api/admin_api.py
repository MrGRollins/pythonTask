from datetime import datetime
from fastapi import APIRouter, Depends
from elastic_search.api.shemas.shop import ShopCreateResponseSchema, ShopCreateRequestSchema, ShopDeleteResponseSchema, \
    ShopDeleteRequestSchema
from elastic_search.core.dependencies.persistance import shop_persistence_dependency
from elastic_search.persistence.common import ShopPersistence


router = APIRouter()

@router.post("/create", summary="Create product", description="Add new in DB product for sale",
             response_model=ShopCreateResponseSchema)
async def create_product(create_request: ShopCreateRequestSchema,
                       shop_persistence :ShopPersistence = Depends(shop_persistence_dependency)) -> ShopCreateResponseSchema:
    product = shop_persistence.save(name=create_request.name, description=create_request.description,
                    count_left=create_request.count_left, create_time=str(datetime.now()), update_time=str(datetime.now()))
    return ShopCreateResponseSchema(id=product.id)


@router.delete("/delete", summary="Delete product", description="Delete product from DB",
             response_model=ShopDeleteResponseSchema)
async def delete_product(delete_request: ShopDeleteRequestSchema,
                       shop_persistence: ShopPersistence = Depends(shop_persistence_dependency)) -> ShopDeleteResponseSchema:
    shop_persistence.delete(name=delete_request.name)
    return ShopDeleteResponseSchema()