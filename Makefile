IMAGE=bnediction/bonesis
TAG=v0

update:
	jupytext --update paper.md --to ipynb --pre-commit-mode --execute
sync:
	jupytext --sync paper.md --to ipynb --pre-commit-mode --execute
source:
	jupytext paper.ipynb --to myst

build-docker:
	docker build -t $(IMAGE):$(TAG) .
test-docker:
	colomoto-docker --image $(IMAGE) -V $(TAG) -e COLOMOTO_SKIP_JUPYTER_JS=1 --bind . jupyter nbconvert --execute --ExecutePreprocessor.timeout=3600 --inplace *.ipynb
