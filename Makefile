MKDOCS = ghcr.io/squidfunk/mkdocs-material:9.0.2

# Run this target and then call `mkdocs serve -a 0.0.0.0:8000` to run a webserver
# Re-run the web server when changes are made to the lexer.
.PHONY: test
test:
	docker run -it --rm -p 8010:8000 \
		-v $(CURDIR)/test:/docs \
		-v $(CURDIR):/command-pygments \
		--entrypoint '' \
		$(MKDOCS) \
		ash -c 'pip install -e /command-pygments && ash'
