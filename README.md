# Aspire EtherCAT Lab

Aspire EtherCAT Lab is a modular development and research platform for EtherCAT-based motion control, industrial communication, and real-time automation systems.

The repository is organized around two future branches:

- `Hardware`: EtherCAT hardware design, schematics, PCB files, BOM, bring-up records, and test documentation.
- `Software`: EtherCAT master/slave software, device configuration, control applications, diagnostics, and test tools.

## Repository Structure

```text
Aspire-EtherCAT-Lab/
├── README.md
├── docs/
│   ├── architecture/
│   ├── protocols/
│   ├── test-reports/
│   └── development-guide/
├── examples/
├── tools/
└── LICENSE
```

Hardware- and software-specific implementation files will be maintained in their corresponding branches.

## Project Goals

- Build a reusable EtherCAT development platform.
- Validate EtherCAT communication and synchronization mechanisms.
- Support distributed clock and real-time control experiments.
- Provide a clear separation between hardware and software development.
- Accumulate reusable design files, test procedures, and engineering documentation.
- Enable future integration with motion-control and industrial automation applications.

## Planned Branches

### `Hardware`

The `Hardware` branch will contain:

- EtherCAT slave and master interface designs
- Schematics and PCB layout files
- Power supply and protection circuits
- Connector and wiring definitions
- Bill of materials
- Manufacturing outputs
- Hardware bring-up and validation records

### `Software`

The `Software` branch will contain:

- EtherCAT master and slave software
- Device configuration files
- PDO and SDO definitions
- Distributed Clock configuration
- Real-time communication tests
- Motion-control examples
- Diagnostics and monitoring tools
- Automated test scripts

## Development Workflow

The default branch stores project-level documentation and integration information.

Feature development should follow this workflow:

1. Create a feature branch from `Hardware` or `Software`.
2. Implement and test the change locally.
3. Update the related documentation and test records.
4. Open a pull request against the corresponding development branch.
5. Merge validated changes into the default branch when the milestone is complete.

Suggested branch naming:

```text
hardware/<feature-name>
software/<feature-name>
docs/<document-name>
test/<test-name>
```

## Documentation

Project documentation should cover:

- System architecture
- EtherCAT network topology
- Device and signal definitions
- Development environment setup
- Build and deployment procedures
- Test plans and test results
- Known issues and compatibility notes

## Status

This project is under active development.

The repository is currently being prepared for the initial separation of hardware and software development branches.

## Roadmap

- [ ] Define EtherCAT system architecture
- [ ] Establish hardware branch
- [ ] Establish software branch
- [ ] Define device and PDO mapping
- [ ] Prepare initial communication test
- [ ] Add distributed clock validation
- [ ] Add hardware bring-up documentation
- [ ] Add automated regression tests
- [ ] Publish the first integrated release

## Contributing

Before submitting changes:

- Keep hardware and software changes in the appropriate branch.
- Include sufficient documentation for new interfaces and configurations.
- Record test conditions and results.
- Avoid committing generated files unless they are required for release or manufacturing.
- Use clear, descriptive commit messages.

## License

This project is distributed under the license specified in [LICENSE](LICENSE).
