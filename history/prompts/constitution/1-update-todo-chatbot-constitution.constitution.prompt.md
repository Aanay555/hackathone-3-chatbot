---
id: 1
title: Update Todo Chatbot Constitution
stage: constitution
date: 2026-01-07
surface: agent
model: Qwen
feature: todo-chatbot
branch: main
user: JUMBO COMPUTERS
command: /sp.constitution
labels: [constitution, todo-chatbot, phase-3]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - null
---

## Prompt

/sp.constitution You are an expert AI system architect specializing in Spec-Driven Development for cloud-native AI applications.

Your task is to create a complete, professional, and detailed **Markdown Constitution** for **Phase III** of the "Hackathon II: Spec-Driven Development" project titled "The Evolution of Todo".

The Constitution must be written in clean, well-structured Markdown format and serve as the foundational governing document for implementing Phase III using strict Spec-Driven Development with Claude Code and Spec-Kit Plus. Remember: no manual coding is allowed — all implementation must be generated via refined specs and Claude Code.

### Project Context
- This is Phase III: AI-Powered Todo Chatbot (200 points, due Dec 21, 2025)
- Builds directly on top of Phase II: a full-stack web Todo app with:
  - Next.js 16+ frontend (App Router)
  - FastAPI backend
  - SQLModel ORM
  - Neon Serverless PostgreSQL database
  - User authentication via Better Auth (JWT-based)
  - REST API endpoints secured per user
  - Monorepo structure with /frontend and /backend folders
- The goal of Phase III is to add a fully conversational AI chatbot interface that allows users to manage their personal Todo list entirely through natural language.

### Core Requirements for Phase III
- Implement a conversational interface using:
  - OpenAI ChatKit
  - OpenAI Agents SDK
  - Official MCP SDK (Multi-Modal Conversation Protocol)
- The chatbot MUST be able to:
  - Understand and execute natural language commands on the user's Todo list
  - Examples: "Add a task to buy groceries tomorrow", "Reschedule my morning meetings to 2 PM", "Mark the gym task as complete", "Show me all incomplete work tasks", "Delete the old project task"
  - Support all Basic Level features via chat: Add, Delete, Update, View, Mark Complete
  - Respect user ownership: only operate on the authenticated user's tasks
- Authentication must flow seamlessly: the chat session must identify the current logged-in user and pass the JWT/context to the agent
- The chatbot should be integrated into the existing Next.js frontend (e.g., as a chat panel or dedicated route)
- Use reusable intelligence patterns (Agent Skills, Subagents) where possible to aim for bonus points

### Constitution Guidelines
The Markdown Constitution must include the following sections with clear, detailed content:

1. **Title & Metadata**
   - Project name, Hackathon name, Phase number, your name/student ID, date

2. **Vision & Objectives**
   - Clear statement of what Phase III achieves and why it matters in the evolution of the Todo app

3. **Scope**
   - What is included in Phase III
   - What is explicitly out of scope (e.g., Phase IV/V deployment, advanced features unless aiming for bonus)

4. **Core Principles**
   - Strict Spec-Driven Development
   - No manual coding
   - Reusability, clean architecture, security, user isolation

5. **Technology Stack for Phase III**
   - List all required and allowed technologies
   - Highlight new additions: OpenAI ChatKit, Agents SDK, Official MCP SDK

6. **Architecture Overview**
   - High-level description of how the chatbot integrates with existing frontend and backend
   - How user authentication flows to the agent
   - How the agent calls existing REST APIs or directly uses tools

7. **Agent Design & Tool Integration**
   - Describe the main agent and any subagents
   - List the MCP tools the agent will have (e.g., create_task, list_tasks, update_task, delete_task, toggle_complete)
   - How tools map to existing FastAPI endpoints
   - Security: how tools enforce user ownership

8. **User Experience**
   - Describe the chat interface in the Next.js app
   - Example conversation flows
   - Error handling and confirmation prompts

9. **Bonus Targets (Optional but Encouraged)**
   - Reusable Intelligence via Agent Skills (+200 possible)
   - Multi-language support (especially Urdu) (+100)
   - Voice commands (+200)

10. **Deliverables for Phase III Submission**
    - Updates to GitHub repo structure
    - New/updated specs in /specs/ folder
    - Demo requirements (video <90 sec)
    - Integration evidence

11. **Success Criteria**
    - What makes this Phase III submission excellent and likely to score full 200 + bonus points

Write the entire Constitution in professional, concise, and inspiring tone. Use proper Markdown formatting: headers, bullet points, tables where appropriate, code blocks for examples.

Output only the final Markdown Constitution — no explanations outside of it.

## Response snapshot

# The Evolution of Todo: Phase III Constitution
<!-- AI-Powered Todo Chatbot Constitution -->

## Core Principles

### I. Strict Spec-Driven Development
All implementation must be generated via refined specs and Claude Code; no manual coding is allowed. Every feature, function, and component must be specified before implementation. Specifications must be detailed enough to generate complete, working code.

### II. No Manual Coding
All code generation must be done through Claude Code based on detailed specifications. Manual coding is strictly prohibited except for specification creation and review. All implementation artifacts must be traceable to specific requirements in the specs.

### III. Reusability and Clean Architecture
Components must be designed for maximum reusability. Clean architecture principles must be followed with clear separation of concerns. Agent Skills and Subagents should be designed as reusable intelligence patterns to enable bonus points.

### IV. Security-First Design
User data isolation is paramount. All operations must respect user ownership boundaries. Authentication context must flow seamlessly through the system. JWT tokens must be properly validated and enforced at all access points.

### V. Test-First Development (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced. All agent interactions must be thoroughly tested for proper functionality and security.

### VI. User Experience Excellence
The conversational interface must be intuitive and natural. Error handling must be graceful with helpful feedback. The chatbot should understand natural language commands and provide clear responses to user actions.

## Technology Stack for Phase III

### Required Technologies
- OpenAI ChatKit for conversational interface
- OpenAI Agents SDK for AI agent implementation
- Official MCP SDK (Multi-Modal Conversation Protocol) for standardized communication
- Next.js 16+ frontend (App Router) - existing from Phase II
- FastAPI backend - existing from Phase II
- SQLModel ORM - existing from Phase II
- Neon Serverless PostgreSQL database - existing from Phase II
- Better Auth for authentication - existing from Phase II

### Integration Points
- REST API endpoints from Phase II will be accessed by the agent
- JWT authentication tokens will flow from frontend to agent
- Existing database schema will be reused for task management

## Architecture Overview

### Chatbot Integration
The AI chatbot will be integrated into the existing Next.js frontend as a dedicated chat panel or route. The architecture maintains the existing backend structure while adding an agent layer that can interact with the existing REST APIs or directly with the database using proper authentication context.

### Authentication Flow
1. User logs in through the existing Better Auth system
2. JWT token is passed to the chat session context
3. The agent receives the authenticated user context for all operations
4. All agent actions are validated against the authenticated user's ownership

### Agent Communication
The agent communicates with the existing backend through:
- Direct API calls to existing REST endpoints
- MCP tools that map to existing backend functionality
- Direct database operations with proper authentication validation

## Agent Design & Tool Integration

### Main Agent Responsibilities
- Process natural language commands from users
- Map commands to appropriate backend operations
- Maintain conversation context and state
- Ensure all operations respect user ownership

### MCP Tools Available
- `create_task`: Add new tasks to the authenticated user's list
- `list_tasks`: Retrieve tasks for the authenticated user
- `update_task`: Modify existing tasks for the authenticated user
- `delete_task`: Remove tasks from the authenticated user's list
- `toggle_complete`: Mark tasks as complete/incomplete for the authenticated user

### Tool Security
All tools must validate that operations are performed only on tasks belonging to the authenticated user. The JWT context must be passed with each tool call to enforce proper access controls.

### Subagent Design
Reusable intelligence patterns (Agent Skills) should be implemented for:
- Natural language understanding and command parsing
- Date/time interpretation for task scheduling
- Confirmation workflows for destructive operations
- Error handling and user feedback

## User Experience

### Chat Interface
The chat interface will be integrated into the existing Next.js application with:
- Real-time conversation display
- Natural language input field
- Visual feedback during processing
- Clear indication of successful operations

### Example Conversation Flows
```
User: "Add a task to buy groceries tomorrow"
Agent: "I've added 'buy groceries' to your list for tomorrow."

User: "Show me all incomplete work tasks"
Agent: "Here are your incomplete work tasks: [list]"

User: "Mark the gym task as complete"
Agent: "I've marked 'gym' as complete."
```

### Error Handling
- Invalid commands will receive helpful suggestions
- Authentication failures will prompt re-authentication
- System errors will be gracefully communicated
- Confirmation prompts for destructive operations

## Bonus Targets (Optional but Encouraged)

### Reusable Intelligence via Agent Skills (+200 possible)
- Implement modular Agent Skills for common operations
- Create reusable components for language processing
- Design extensible skill architecture for future features

### Multi-language support (especially Urdu) (+100)
- Implement language detection and translation
- Support natural language processing in Urdu
- Maintain consistent functionality across languages

### Voice commands (+200)
- Integrate speech-to-text capabilities
- Support voice-based task management
- Provide text-to-speech responses

## Deliverables for Phase III Submission

### GitHub Repo Updates
- New/updated specs in /specs/ folder
- Complete implementation following SDD principles
- Updated documentation and usage guides
- Demo video (under 90 seconds) showing functionality

### Specification Artifacts
- Detailed architecture specification
- Agent design and tool specifications
- User experience flow specifications
- Security and authentication specifications

### Integration Evidence
- Working demo of all Basic Level features via chat
- Authentication flow demonstration
- Error handling and security validation
- Bonus feature implementations (if attempted)

## Success Criteria

### Excellence Requirements
- Complete implementation of all Basic Level features via natural language
- Seamless integration with existing Phase II architecture
- Proper authentication flow with user isolation
- Clean, maintainable code generated through SDD process
- Comprehensive testing of all functionality

### Bonus Achievement
- Successful implementation of reusable Agent Skills
- Multi-language support (especially Urdu)
- Voice command functionality
- Additional innovative features that enhance user experience

### Scoring Targets
- Full 200 points for core requirements
- Up to 500 additional points for bonus features
- Clean, well-documented, and maintainable codebase
- Adherence to all SDD principles and no manual coding

## Governance

This constitution governs all development activities for Phase III of the "The Evolution of Todo" project. All implementation must adhere to the principles of Spec-Driven Development with no manual coding. Amendments to this constitution require explicit documentation and approval from project stakeholders.

All pull requests and code reviews must verify compliance with these principles. Any deviation from SDD methodology or introduction of manually coded components will result in rejection.

**Version**: 1.0.0 | **Ratified**: 2026-01-07 | **Last Amended**: 2026-01-07

## Outcome

- ✅ Impact: Created a comprehensive constitution for the Todo Chatbot Phase III project that establishes the foundational principles for Spec-Driven Development implementation
- 🧪 Tests: No tests required for constitution creation
- 📁 Files: Updated .specify/memory/constitution.md with the new constitution
- 🔁 Next prompts: Ready to proceed with feature specification using /sp.specify
- 🧠 Reflection: The constitution clearly defines the core principles, technology stack, architecture, and success criteria for the AI-powered Todo chatbot project, ensuring all development follows Spec-Driven Development methodology without manual coding.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Begin creating feature specifications based on the established constitution