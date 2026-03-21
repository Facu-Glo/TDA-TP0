SCRIPT = amigos.py
GRAFICO = Graficos.graficos
VENV = venv
PYTHON = python3
BIN = $(VENV)/bin/python
LIBRERIAS = numpy matplotlib

LATEX = pdflatex
INFORME_DIR = Informe
INFORME_TEX = informe.tex
BUILD_DIR = $(INFORME_DIR)/build

.PHONY: install run graphics pdf clean

install:
	@$(PYTHON) -m venv $(VENV)
	@$(BIN) -m pip install --upgrade pip
	@$(BIN) -m pip install $(LIBRERIAS)

run:
	@$(BIN) $(SCRIPT)

graphics:
	@$(BIN) -m $(GRAFICO)

pdf:
	@mkdir -p $(BUILD_DIR)
	@$(LATEX) -output-directory=$(BUILD_DIR) $(INFORME_DIR)/$(INFORME_TEX)
	@$(LATEX) -output-directory=$(BUILD_DIR) $(INFORME_DIR)/$(INFORME_TEX)
	@mv $(BUILD_DIR)/$(INFORME_TEX:.tex=.pdf) $(INFORME_DIR)/

clean:
	@rm -rf $(VENV) $(BUILD_DIR)
	@rm -rf $(INFORME_DIR)/$(INFORME_TEX:.tex=.pdf)
	@find . -type d -name "__pycache__" -exec rm -rf {} +
