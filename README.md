# Pluto LM

Pluto is a small language model built from scratch, to learn and experiment with LLM architecture, training, and scaling.

## About

This repo tracks the development of Pluto across several planned model sizes and variants, starting small and scaling up as the codebase and training pipeline mature.
Pluto models will be available on Hugging Face at https://huggingface.co/raduparaian, when they are ready.

## Roadmap

- [ ] **Pluto v1 100M**: Initial small-scale model & proof of concept
- [ ] **Pluto v1 500M**: Mid-size scaled up model
- [ ] **Pluto v1.5 1B**: Second-generation, larger, denser, model
- [ ] **Pluto v1.5 MoE**: Mixture-of-experts variant built upon Pluto v1.5
- [ ] **Pluto v1.5 Vision**: Vision-language variant built upon Pluto v1.5

## Status

Early development. Architecture, training data, and benchmarks will be documented here as they're finalized.

## Goals

- Build and train a transformer-based LLM from the ground up
- Understand scaling behavior across model sizes
- Explore MoE architectures for efficient scaling
- Extend to multimodal (vision + language) capabilities

## Usage

_Coming soon — training and inference instructions will be added once the first checkpoint (Pluto v1 100M) is ready._

## License

Apache 2.0

## Acknowledgements

Built as a learning project exploring modern LLM architecture and training techniques.
