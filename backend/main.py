from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
from collections import deque

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request model
class PipelineData(BaseModel):
    nodes: List[Dict[str, Any]]
    edges: List[Dict[str, Any]]

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
async def parse_pipeline(pipeline: PipelineData):
    try:
        nodes = pipeline.nodes
        edges = pipeline.edges
        
        num_nodes = len(nodes)
        num_edges = len(edges)
        is_dag = check_dag(nodes, edges)
        
        return {
            'num_nodes': num_nodes,
            'num_edges': num_edges,
            'is_dag': is_dag
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def check_dag(nodes, edges):
    """Check if the pipeline forms a Directed Acyclic Graph"""
    if not nodes:
        return True
    
    # Build graph
    graph = {node['id']: [] for node in nodes}
    in_degree = {node['id']: 0 for node in nodes}
    
    # Add edges to graph
    for edge in edges:
        source = edge.get('source')
        target = edge.get('target')
        
        # Skip if source or target doesn't exist
        if source not in graph or target not in graph:
            continue
            
        graph[source].append(target)
        in_degree[target] += 1
    
    # Kahn's algorithm for cycle detection
    queue = deque([node_id for node_id in graph if in_degree[node_id] == 0])
    visited_count = 0
    
    while queue:
        node_id = queue.popleft()
        visited_count += 1
        
        for neighbor in graph[node_id]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If visited all nodes, it's a DAG
    return visited_count == len(nodes)