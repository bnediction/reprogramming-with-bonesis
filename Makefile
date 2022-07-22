IMAGE=bnediction/bonesis
TAG=v0

build:
	docker build -t $(IMAGE):$(TAG) .

test:
	colomoto-docker --image $(IMAGE) -V $(TAG) -e COLOMOTO_SKIP_JUPYTER_JS=1 --bind . jupyter nbconvert --execute --ExecutePreprocessor.timeout=3600 --inplace *.ipynb
