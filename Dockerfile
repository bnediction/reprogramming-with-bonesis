FROM colomoto/colomoto-docker:2022-07-01

USER root
RUN conda install bonesis

USER user
RUN rm -rf /notebook/*
COPY --chown=user:user . /notebook/
