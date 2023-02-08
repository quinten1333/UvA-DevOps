# Links
- https://github.com/quinten1333/UvA-DevOps/tree/week1
- https://app.swaggerhub.com/apis/quinten1333/DevOps-week1/1.0.0
- https://hub.docker.com/r/amicopo/uva_devops_wk1

# Swagger API
```yaml
openapi: 3.0.0
servers:
  # Added by API Auto Mocking Plugin
  - description: SwaggerHub API Auto Mocking
    url: https://virtserver.SwaggerHub.com/tutorial/1.0.0
info:
  description: This is a simple API
  version: "1.0.0"
  title: Simple Inventory API
  contact:
    email: you@your-company.com
  license:
    name: Apache 2.0
    url: 'http://www.apache.org/licenses/LICENSE-2.0.html'
paths:
  /student/{student_id}:
    get:
      summary: gets student
      operationId: getStudentById
      description: |
        Returns a single student
      parameters:
        - in: path
          name: student_id
          description: the uid
          required: true
          schema:
            type: number
            format: integer
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Student'
        '400':
          description: invalid ID
        '404':
          description: not found
    delete:
      summary: deletes a student
      description: delete a single student
      operationId: delete_student
      parameters:
      - name: student_id
        in: path
        description: the uid
        required: true
        schema:
          type: number
          format: integer
      responses:
        "200":
          description: Student has been found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Student'
        "400":
          description: Invalid student_id provided
        "404":
          description: User not found
  /student:
    post:
      summary: Add a new student
      operationId: addStudent
      description: Adds an item to the system
      responses:
        '200':
          description: created
          content:
            application/json:
              schema:
                type: number
                format: integer
        '400':
          description: 'invalid input, object invalid'
        '409':
          description: an existing already exists
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Student'
        description: Student item to add
components:
  schemas:
    Student:
      type: object
      required:
      - first_name
      - last_name
      properties:
        student_id:
          type: number
          format: integer
        first_name:
          type: string
        last_name:
          type: string
          example: Coltof
        gradeRecords:
          type: array
          items:
            type: number
      example:
        first_name: Quinten
        last_name: Coltof
        gradeRecord: [8, 9, 10]

    GradeRecord:
      type: object
      required:
      - subject_name
      - grade
      properties:
        subject_name:
          type: string
        grade:
          type: number
          format: float
          minimum: 0
          maximum: 10
      example:
        subject_name: Quinten Coltof
        grade: 10
```

# DevOps stages
- Plan: Creating the schema is planning
- Code: Making a functioning server and implementing MongoDB
- Build: Using docker to build a docker image
- Test: Using potman to test the implementation
- Release: Publishing to docker hub
- Deploy: Running the docker-compose.yml. This step is not really thorough but a small part is there.

# OpenAPI Exercises
## Define objects
The schema for the components are defined using the documentation on https://swagger.io/specification/. Adding examples was done using the documentation https://swagger.io/docs/specification/adding-examples/

## Add delete method
The delete method is made by duplicating the get method and updating the description and naming to delete instead of the wording get and create.

# Development environment
For developing I have created a `Dockerfile-dev` and matching `docker-compose.yml` which runs the application within docker with hot reloading. This is done by linking the directory as a volume in docker and by utilising `nodemon` an application which reloads the applications on changes. To run nodemon, nodejs and npm need to be installed which is why a separate Dockerfile is necessary.

# MongoDB Integration
First a library has to be found to connect to MongoDB. I chose to use `pymongo` for this because it is used often and is well documented.

Then the MONGO_URI environment variable has to be extracted and a connection made to the MongoDB.

Once there is a connection the functions have to be modified to query, insert and delete the records properly into MongoDB instead of TinyDB. After this the implementation is done. So only the service file has to be edited for this change.

# Question 1
Alpine images have the [alpine system](https://hub.docker.com/_/alpine) as the base layer which is extremely small. Quoting from their documentation ``The image is only 5 MB in size and has access to a package repository that is much more complete than other BusyBox based images''. Due to this it is good practice to develop from a ubuntu base image for example and then build using alpine as base image for production.
