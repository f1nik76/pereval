# API Schema
REST API

## Version: 1.0

### /submitData/

#### GET

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user__email | query | user__email | No | string |

##### Responses

| Code | Description |
| ---- |-------------|
| 200 | OK          |

#### POST

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description |
| ---- |-------------|
| 201 | Created     |

### /submitData/{id}/

#### GET



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this pereval. | Yes | string |
| user__email | query | user__email | No | string |

##### Responses

| Code | Description |
| ---- |-------------|
| 200 | OK           |

#### PUT



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this pereval. | Yes | string |
| user__email | query | user__email | No | string |

##### Responses

| Code | Description |
| ---- |-------------|
| 200 | OK          |

#### PATCH



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this pereval. | Yes | string |
| user__email | query | user__email | No | string |

##### Responses

| Code | Description |
| ---- |-------------|
| 200 | OK          |

#### DELETE
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this pereval. | Yes | string |
| user__email | query | user__email | No | string |

##### Responses

| Code | Description |
| ---- |-------------|
| 204 | No content  |