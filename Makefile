imageName=amicopo/uva_devops_wk1

.phony: build push

build:
	docker build -t ${imageName} .

push:
	docker push ${imageName}

run:
	docker run -it --rm -p 8080:8080 ${imageName}
