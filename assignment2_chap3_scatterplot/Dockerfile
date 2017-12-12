FROM tensorflow/tensorflow:latest-py3
LABEL maintainer = "zia@panacloud.com"
RUN find /notebooks -delete
COPY . /notebooks
WORKDIR "/notebooks"
CMD ["/run_jupyter.sh", "--allow-root"]
