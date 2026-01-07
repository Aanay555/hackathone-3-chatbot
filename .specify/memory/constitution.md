# Hackathon II – Phase III: AI-Powered Todo Chatbot Constitution

**Student Name:** [STUDENT_NAME]

**Date:** January 2026

**Points:** 200 + Bonus Targets

## Vision Statement

Welcome to the next evolution of the Todo application! We're transforming a traditional task management system into an intelligent AI-native platform that understands natural language and responds with human-like interactions. This Phase III implementation will revolutionize how users interact with their task lists, making productivity more intuitive and accessible than ever before. Through the power of OpenAI's ChatKit and Agent SDK, we're creating a seamless bridge between human communication and digital task management.

## Objectives of Phase III

- Integrate an AI chatbot that allows complete Todo list management via natural language
- Implement secure user authentication flow to the agent system
- Design reusable Agent Skills for maximum intelligence reusability (bonus target)
- Create a beautiful UI with blue and pink theme integrated into existing Next.js frontend
- Ensure strict adherence to Spec-Driven Development methodology with zero manual coding
- Implement MCP tools that securely interact with existing backend services

## Scope

### In Scope
- Chatbot integration with natural language processing for CRUD operations
- User authentication and data isolation using JWT tokens
- Secure MCP tools that interact with existing FastAPI endpoints
- Beautiful UI implementation with blue and pink theme
- Reusable Agent Skills for bonus points
- Complete integration with existing Phase II architecture

### Out of Scope
- Kubernetes deployment (reserved for Phase IV/V)
- Advanced features beyond the core chatbot functionality (unless for bonus)
- Major architectural changes to existing Phase II components

## Core Principles

### I. Strict Spec-Driven Development
All implementation must be generated via refined specs and Claude Code; no manual coding is allowed. Every feature, function, and component must be specified before implementation. Specifications must be detailed enough to generate complete, working code.

### II. No Manual Coding
All code generation must be done through Claude Code based on detailed specifications. Manual coding is strictly prohibited except for specification creation and review. All implementation artifacts must be traceable to specific requirements in the specs.

### III. Security & User Data Isolation
User data privacy and isolation is paramount. All operations must respect user ownership boundaries. Authentication context must flow seamlessly through the system. JWT tokens must be properly validated and enforced at all access points.

### IV. Reusability (Agent Skills)
Components must be designed for maximum reusability. Agent Skills and Subagents should be designed as reusable intelligence patterns to enable bonus points. Clean architecture principles must be followed with clear separation of concerns.

### V. Clean Architecture
Maintain clear separation of concerns with well-defined boundaries between components. The architecture should be modular, testable, and maintainable. Follow established patterns for component interaction.

### VI. Beautiful UI (Blue & Pink theme)
The user interface must be aesthetically pleasing with a consistent blue and pink color scheme. The chat interface should be intuitive, responsive, and provide excellent user experience. Visual design should enhance usability.

## Existing Foundation (from Phase II)

Our solid foundation includes:
- Next.js 16+ frontend with App Router
- FastAPI backend with secure REST APIs
- SQLModel ORM for database operations
- Neon Serverless PostgreSQL for data storage
- Better Auth for JWT-based authentication
- Proper monorepo structure with clear separation of concerns
- Multi-user support with proper data isolation

## Technology Stack for Phase III

| Component | Technology | Purpose |
|-----------|------------|---------|
| Frontend | Next.js 16+ (App Router) | Existing UI framework |
| Backend | FastAPI | Existing API framework |
| Database | Neon Serverless PostgreSQL | Existing data storage |
| Authentication | Better Auth | Existing JWT system |
| AI Chat Interface | OpenAI ChatKit | Natural language processing |
| AI Agent | OpenAI Agents SDK | Task management logic |
| Communication Protocol | Official MCP SDK | Standardized tool interactions |
| ORM | SQLModel | Existing database operations |

## High-Level Architecture

The integration follows this flow:
```
Next.js Chat UI → sends message + JWT → ChatKit → Agent → MCP Tools → FastAPI → Database
```

Authentication is passed securely through the system:
1. User authenticates via existing Better Auth system
2. JWT token is passed to the chat session context
3. Agent receives authenticated user context for all operations
4. MCP tools validate user ownership for all database operations
5. All responses are filtered to respect user data isolation

## Agent Design

### Main Agent: Todo Assistant
- **Role**: Personal task management assistant that understands natural language
- **Responsibilities**: Process commands, maintain conversation context, ensure security
- **State Management**: Stateless conversation handling with context awareness

### Subagents/Agent Skills for Reusability (Bonus)
- **Language Parser Skill**: Interpret natural language commands
- **Date/Time Interpreter Skill**: Handle scheduling and due dates
- **Confirmation Skill**: Handle destructive operations with user confirmation
- **Error Handler Skill**: Manage errors gracefully with user feedback

## MCP Tools Specification

The agent will have access to these specific tools:

### create_task(title, description, due_date?)
- Creates a new task for the authenticated user
- Validates user ownership via JWT context
- Returns confirmation of task creation

### list_tasks(status?, priority?)
- Retrieves tasks for the authenticated user only
- Filters based on optional status and priority parameters
- Respects user ownership via JWT validation

### update_task(id, new_fields)
- Updates specific fields of an existing task
- Validates that task belongs to authenticated user
- Returns updated task information

### delete_task(id)
- Removes a task from the user's list
- Validates user ownership before deletion
- Returns confirmation of deletion

### toggle_complete(id)
- Marks a task as complete or incomplete
- Validates user ownership before update
- Returns updated task status

### search_tasks(keyword)
- Searches user's tasks for matching keywords
- Respects user data isolation
- Returns matching tasks with relevant information

Each tool enforces user ownership via JWT/user_id validation to ensure data security.

## Database & Models Reminder

The existing Task model includes:
- `id`: Unique identifier
- `user_id`: Foreign key to authenticated user
- `title`: Task title
- `description`: Task description
- `completed`: Boolean indicating completion status
- `due_date`: Optional due date/time
- `priority`: Task priority level
- `created_at`: Timestamp of creation
- `updated_at`: Timestamp of last update

## Chat Interface UI/UX

The integrated chat panel in Next.js will feature:
- **Color Scheme**: Primary blue (#2563eb) with pink accents (#ec4899)
- **Message Bubbles**: Different styling for user vs agent messages
- **Loading States**: Visual indicators during AI processing
- **Error Handling**: Clear, helpful error messages
- **Responsive Design**: Works on all device sizes
- **Accessibility**: Proper ARIA labels and keyboard navigation

Example conversation flow:
```
User: "Add a task to buy milk tomorrow at 5 PM"
Agent: "I've added 'buy milk' to your list for tomorrow at 5:00 PM."

User: "Show me all my incomplete tasks"
Agent: "Here are your incomplete tasks: [list with titles and due dates]"

User: "Mark the gym task as complete"
Agent: "I've marked 'gym' as complete. Great job!"
```

## Natural Language Examples

1. "Add a task to buy milk tomorrow at 5 PM" → Creates new task with due date
2. "Show me all my incomplete tasks" → Lists all incomplete tasks
3. "Mark the gym task as complete" → Updates task status to complete
4. "Delete the old project meeting task" → Removes specified task
5. "Reschedule my morning meeting to 3 PM" → Updates due date of existing task
6. "What tasks do I have for today?" → Lists tasks due today
7. "Set high priority for the report task" → Updates task priority
8. "Remind me about the doctor appointment next week" → Creates task with future date
9. "Show me urgent tasks" → Lists tasks with high priority
10. "Clear all completed tasks" → Deletes all completed tasks
11. "What's on my list for this weekend?" → Lists tasks for the weekend
12. "Update the grocery task to include bananas" → Modifies task description

## Error Handling & Safety

### Ambiguous Commands
- When a command is unclear, the agent will ask for clarification
- Example: "Which task do you want me to mark as complete?"

### Invalid Task ID
- The agent will respond politely when a task ID doesn't exist
- Example: "I couldn't find that task in your list. Would you like me to show you your tasks?"

### Unauthorized Access
- The system will never expose other users' data
- All operations are validated against the authenticated user's ownership
- Security failures result in appropriate error responses without data exposure

## Bonus Targets

### Reusable Intelligence via Agent Skills (+200)
- Implement modular Agent Skills for common operations
- Create reusable components for language processing
- Design extensible skill architecture for future features

### Clean Separation for Future Urdu Support (+100 possible later)
- Implement language detection and translation capabilities
- Support natural language processing in Urdu
- Maintain consistent functionality across languages

### Modular Design for Voice (Future +200)
- Prepare architecture for speech-to-text integration
- Design for voice command functionality
- Plan for text-to-speech responses

## Deliverables for Phase III

### Updated Monorepo Structure
- New/updated specifications in `/specs/features/chatbot.md`
- MCP tools specification in `/specs/api/mcp-tools.md`
- Agent design documentation in `/specs/agents/main-agent.md`

### Implementation Artifacts
- Complete AI chatbot implementation following SDD principles
- Updated frontend with chat interface
- MCP tools implementation
- Agent skills and subagents (for bonus)

### Documentation
- Updated README with chatbot usage instructions
- Architecture documentation
- API documentation for new endpoints

### Demo Requirements
- Demo video under 90 seconds showing all functionality
- GitHub repo with complete implementation
- Clear setup and run instructions

## Success Criteria

### Core Functionality (200 points)
- Complete implementation of all natural language CRUD operations
- Proper user authentication and data isolation
- Beautiful UI with blue and pink theme
- Clean, maintainable code generated through SDD
- Zero manual coding violations

### Bonus Achievement Potential (up to 500 additional points)
- Successful implementation of reusable Agent Skills (+200)
- Multi-language support preparation (+100)
- Voice command architecture preparation (+200)
- Additional innovative features that enhance user experience

### Excellence Indicators
- Full functionality with intuitive natural language processing
- Seamless integration with existing Phase II architecture
- Proper security implementation with user data isolation
- Clean, well-documented, and maintainable codebase
- Adherence to all SDD principles and no manual coding

## Governance

This constitution governs all development activities for Phase III of the "The Evolution of Todo" project. All implementation must adhere to the principles of Spec-Driven Development with no manual coding. Amendments to this constitution require explicit documentation and approval from project stakeholders.

All pull requests and code reviews must verify compliance with these principles. Any deviation from SDD methodology or introduction of manually coded components will result in rejection.

**Version**: 1.0.0 | **Ratified**: 2026-01-07 | **Last Amended**: 2026-01-07