## Standard auth flow stuff (allauth?)

- [ ] Sign up
- [ ] Sign in
- [ ] Verify email
- [ ] Reset password

## AOI CRUD

_Areas of Interest_ should allow you to create an AOI that filters down cases.

- [ ] List AOIs: show all AOIs available in the system or created by the user.
- [ ] View AOI:
  - [ ] show details about a specific AOI;
  - [ ] show the list of cases that match its filter;
  - [ ] give access to edit it if owned;
  - [ ] show user's active alerts;
  - [ ] give ability to create alert regardless of ownership.
- [ ] Create AOI:
  - [ ] define geoshape, set a name, and customize alert settings.
- [ ] Update AOI: rename, redefine boundaries; action to delete;
- [ ] Delete AOI, will cascade delete any alerts set up for it.

## Cases R
- [ ] View details about an individual case:
  - [ ] Case Metadata
    - case_number
    - case_url
    - case_date
    - case_type
  - [ ] Case Details
    - location
    - geometry_pnt
    - parcel_number
    - description
    - owner
  - [ ] System Metadata
    - created_at
    - updated_at

## Alert CRUD

- [ ] Create Alert: Given an AOI, create an alert for it.
- [ ] List Alerts:
  - do you want individual alerts or include in a digest (daily, weekly, monthly)?
- [ ] Update: change frequency
- [ ] Delete: remove alert