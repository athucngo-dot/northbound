
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app.schemas.organization import OrganizationCreateRequest, OrganizationRead
from app.services.organization_service import OrganizationService
from app.api.deps import get_current_user, get_db
from app.services.organization_member_service import OrganizationMemberService
from app.schemas.organization_member import MyOrganizationRead


router = APIRouter(prefix="/organizations", tags=["organizations"])

# Get all organizations the current user belongs to, with their membership status
@router.get("/me", response_model=list[MyOrganizationRead])
def get_my_organizations(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    service = OrganizationMemberService(db)
    my_orgs = service.get_user_memberships(current_user)

    return my_orgs

# Create a new organization and automatically become its owner
@router.post("/", response_model=OrganizationRead)
def create_organization(
    org: OrganizationCreateRequest,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
   service = OrganizationService(db)
   new_org = service.create_my_organization(current_user, org)

   return new_org