import { useEffect, useMemo } from 'react';
import ReactFlow, {
  Node,
  Edge,
  Background,
  Controls,
  MiniMap,
  useNodesState,
  useEdgesState,
} from 'reactflow';
import dagre from 'dagre';
import { FlowchartData } from './flowchart-data';
import 'reactflow/dist/style.css';

interface FlowchartViewProps {
  visitedNodes: string[];
  flowchart: FlowchartData;
}

const dagreGraph = new dagre.graphlib.Graph();
dagreGraph.setDefaultEdgeLabel(() => ({}));

const nodeWidth = 200;
const nodeHeight = 80;

const getLayoutedElements = (
  nodes: Node[],
  edges: Edge[],
  direction = 'TB'
) => {
  const isHorizontal = direction === 'LR';
  dagreGraph.setGraph({ 
    rankdir: direction,
    nodesep: 100,    // Horizontal spacing between nodes
    ranksep: 150,    // Vertical spacing between levels
    marginx: 50,
    marginy: 50
  });

  nodes.forEach((node) => {
    dagreGraph.setNode(node.id, { width: nodeWidth, height: nodeHeight });
  });

  edges.forEach((edge) => {
    dagreGraph.setEdge(edge.source, edge.target);
  });

  dagre.layout(dagreGraph);

  const layoutedNodes = nodes.map((node) => {
    const nodeWithPosition = dagreGraph.node(node.id);
    return {
      ...node,
      position: {
        x: nodeWithPosition.x - nodeWidth / 2,
        y: nodeWithPosition.y - nodeHeight / 2,
      },
    };
  });

  return { nodes: layoutedNodes, edges };
};

const getNodeStyle = (nodeType: string, isVisited: boolean) => {
  const baseStyle = {
    padding: '16px',
    borderRadius: nodeType === 'decision' ? '4px' : '12px',
    fontSize: '12px',
    width: `${nodeWidth}px`,
    height: `${nodeHeight}px`,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    textAlign: 'center' as const,
    border: '2px solid',
    transition: 'all 0.3s ease',
  };

  if (isVisited) {
    if (nodeType === 'start') {
      return {
        ...baseStyle,
        background: 'linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%)',
        borderColor: '#3b82f6',
        color: '#ffffff',
        fontWeight: '600',
        boxShadow: '0 4px 12px rgba(59, 130, 246, 0.4)',
      };
    } else if (nodeType === 'end') {
      return {
        ...baseStyle,
        background: 'linear-gradient(135deg, #fee2e2 0%, #fecaca 100%)',
        borderColor: '#ef4444',
        color: '#7f1d1d',
        fontWeight: '600',
        boxShadow: '0 4px 12px rgba(239, 68, 68, 0.3)',
      };
    } else {
      return {
        ...baseStyle,
        background: 'linear-gradient(135deg, #f3e8ff 0%, #e9d5ff 100%)',
        borderColor: '#8b5cf6',
        color: '#5b21b6',
        fontWeight: '500',
        boxShadow: '0 4px 12px rgba(139, 92, 246, 0.3)',
      };
    }
  } else {
    return {
      ...baseStyle,
      background: '#ffffff',
      borderColor: nodeType === 'end' ? '#fca5a5' : '#d1d5db',
      color: nodeType === 'end' ? '#7f1d1d' : '#374151',
      opacity: 0.8,
    };
  }
};

export function FlowchartView({ visitedNodes, flowchart }: FlowchartViewProps) {
  if (!flowchart || !flowchart.nodes || !flowchart.edges) {
    return (
      <div className="h-full flex items-center justify-center text-gray-500">
        Loading flowchart...
      </div>
    );
  }

  // Convert flowchart data to React Flow format
  const initialNodes: Node[] = flowchart.nodes.map((node) => ({
    id: node.id,
    data: { label: node.label },
    type: 'default',
    style: getNodeStyle(node.type, visitedNodes.includes(node.id)),
    position: { x: 0, y: 0 }, // Will be positioned by Dagre
  }));

  const initialEdges: Edge[] = flowchart.edges.map((edge, idx) => {
    const isVisited = visitedNodes.includes(edge.from) && visitedNodes.includes(edge.to);
    
    return {
      id: `edge-${idx}`,
      source: edge.from,
      target: edge.to,
      label: edge.label || undefined,
      animated: isVisited,
      style: {
        stroke: isVisited ? '#8b5cf6' : '#d1d5db',
        strokeWidth: isVisited ? 2.5 : 1.5,
      },
      labelStyle: {
        fontSize: '11px',
        fontWeight: isVisited ? '600' : '500',
        fill: isVisited ? '#7c3aed' : '#6b7280',
      },
    };
  });

  // Apply Dagre layout
  const { nodes: layoutedNodes, edges: layoutedEdges } = useMemo(
    () => getLayoutedElements(initialNodes, initialEdges),
    [flowchart]
  );

  const [nodes, setNodes, onNodesChange] = useNodesState(layoutedNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(layoutedEdges);

  // Update node styles when visitedNodes changes
  useEffect(() => {
    setNodes((nds) =>
      nds.map((node) => ({
        ...node,
        style: getNodeStyle(
          flowchart.nodes.find(n => n.id === node.id)?.type || 'question',
          visitedNodes.includes(node.id)
        ),
      }))
    );
    
    setEdges((eds) =>
      eds.map((edge) => {
        const isVisited = visitedNodes.includes(edge.source) && visitedNodes.includes(edge.target);
        return {
          ...edge,
          animated: isVisited,
          style: {
            stroke: isVisited ? '#8b5cf6' : '#d1d5db',
            strokeWidth: isVisited ? 2.5 : 1.5,
          },
        };
      })
    );
  }, [visitedNodes, flowchart]);

  return (
    <div className="h-full flex flex-col p-5">
      <div className="mb-4">
        <h3 className="text-gray-900 mb-1">Your Diagnostic Path</h3>
        <p className="text-xs text-purple-600">
          Highlighted nodes show your current path
        </p>
      </div>
      
      <div className="flex-1 bg-white rounded-lg border border-gray-200" style={{ minHeight: '600px' }}>
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          fitView
          attributionPosition="bottom-left"
          minZoom={0.5}
          maxZoom={1.5}
          defaultViewport={{ x: 0, y: 0, zoom: 0.9 }}
          proOptions={{ hideAttribution: true }}
        >
          <Background color="#f3f4f6" gap={16} />
          <Controls showInteractive={false} />
          <MiniMap
            nodeColor={(node) => {
              const isVisited = visitedNodes.includes(node.id);
              return isVisited ? '#8b5cf6' : '#e5e7eb';
            }}
            maskColor="rgba(0, 0, 0, 0.05)"
            style={{ backgroundColor: '#f9fafb' }}
          />
        </ReactFlow>
      </div>
    </div>
  );
}
