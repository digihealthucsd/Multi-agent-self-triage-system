import { FlowchartData } from './flowchart-data';
import { Button } from './ui/button';
import { Check } from 'lucide-react';

interface FlowchartSelectionPageProps {
  recommendedFlowchart: FlowchartData;
  similarFlowcharts: FlowchartData[];
  onSelectFlowchart: (flowchart: FlowchartData) => void;
}

export function FlowchartSelectionPage({
  recommendedFlowchart,
  similarFlowcharts,
  onSelectFlowchart,
}: FlowchartSelectionPageProps) {
  
  // Render a mini preview of the flowchart
  const renderFlowchartPreview = (flowchart: FlowchartData) => {
    if (!flowchart || !flowchart.nodes || flowchart.nodes.length === 0) {
      return null;
    }
    
    const nodes = flowchart.nodes;
    const edges = flowchart.edges || [];
    
    // Calculate viewBox based on node positions
    const minX = Math.min(...nodes.map(n => n.x - n.width / 2)) - 20;
    const minY = Math.min(...nodes.map(n => n.y - n.height / 2)) - 20;
    const maxX = Math.max(...nodes.map(n => n.x + n.width / 2)) + 20;
    const maxY = Math.max(...nodes.map(n => n.y + n.height / 2)) + 20;
    
    const viewBoxWidth = maxX - minX;
    const viewBoxHeight = maxY - minY;

    const getNodePath = (node: typeof nodes[0]) => {
      const x = node.x - node.width / 2;
      const y = node.y - node.height / 2;

      if (node.type === 'decision') {
        // Diamond shape
        return `M ${node.x} ${y} L ${x + node.width} ${node.y} L ${node.x} ${y + node.height} L ${x} ${node.y} Z`;
      } else {
        // Rounded rectangle
        const radius = node.type === 'start' ? 25 : 12;
        return `M ${x + radius} ${y} 
                L ${x + node.width - radius} ${y} 
                Q ${x + node.width} ${y} ${x + node.width} ${y + radius}
                L ${x + node.width} ${y + node.height - radius}
                Q ${x + node.width} ${y + node.height} ${x + node.width - radius} ${y + node.height}
                L ${x + radius} ${y + node.height}
                Q ${x} ${y + node.height} ${x} ${y + node.height - radius}
                L ${x} ${y + radius}
                Q ${x} ${y} ${x + radius} ${y} Z`;
      }
    };

    return (
      <svg
        viewBox={`${minX} ${minY} ${viewBoxWidth} ${viewBoxHeight}`}
        className="w-full h-full"
        preserveAspectRatio="xMidYMid meet"
      >
        <defs>
          <marker
            id={`arrow-${flowchart.id}`}
            markerWidth="10"
            markerHeight="10"
            refX="9"
            refY="3"
            orient="auto"
          >
            <polygon points="0 0, 10 3, 0 6" fill="#d1d5db" />
          </marker>
        </defs>

        {/* Draw edges */}
        {edges.map((edge, idx) => {
          if (!edge || !edge.from || !edge.to) return null;
          
          const fromNode = nodes.find((n) => n.id === edge.from);
          const toNode = nodes.find((n) => n.id === edge.to);
          
          if (!fromNode || !toNode) return null;

          const fromX = fromNode.x;
          const fromY = fromNode.y + fromNode.height / 2;
          const toX = toNode.x;
          const toY = toNode.y - toNode.height / 2 - 5;

          return (
            <line
              key={`edge-${idx}`}
              x1={fromX}
              y1={fromY}
              x2={toX}
              y2={toY}
              stroke="#d1d5db"
              strokeWidth={1.5}
              markerEnd={`url(#arrow-${flowchart.id})`}
              opacity={0.6}
            />
          );
        })}

        {/* Draw nodes */}
        {nodes.map((node) => {
          if (!node || !node.id) return null;
          
          let fillColor = '#ffffff';
          let strokeColor = '#d1d5db';
          
          if (node.type === 'end') {
            strokeColor = '#fca5a5';
          }

          return (
            <g key={node.id}>
              <path
                d={getNodePath(node)}
                fill={fillColor}
                stroke={strokeColor}
                strokeWidth={1.5}
                opacity={0.95}
              />
            </g>
          );
        })}
      </svg>
    );
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-white via-blue-50/30 to-purple-50/30 flex flex-col">
      {/* Header */}
      <div className="bg-white/80 backdrop-blur-sm border-b border-gray-200 sticky top-0 z-10">
        <div className="px-6 py-4">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
              <svg 
                className="w-5 h-5 text-white" 
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path 
                  strokeLinecap="round" 
                  strokeLinejoin="round" 
                  strokeWidth={2} 
                  d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" 
                />
                <path 
                  strokeLinecap="round" 
                  strokeLinejoin="round" 
                  strokeWidth={2.5} 
                  d="M12 9v6M9 12h6" 
                />
              </svg>
            </div>
            <div>
              <div className="text-sm text-gray-500">TriageMD</div>
              <div className="text-xs text-gray-400">AMA Compliant</div>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-y-auto px-6 py-8">
        <div className="max-w-5xl mx-auto">
          {/* Title */}
          <div className="mb-8 text-center">
            <h2 className="text-gray-900 mb-2">Flowchart Selection</h2>
            <p className="text-gray-600">
              Based on your input, we think <span className="font-medium text-purple-600">{recommendedFlowchart.name}</span> is most appropriate for you.
            </p>
          </div>

          {/* Recommended Flowchart */}
          <div className="mb-8">
            <div className="bg-gradient-to-br from-purple-50 to-blue-50 rounded-xl p-6 border-2 border-purple-300 relative">
              <div className="absolute -top-3 left-6 bg-gradient-to-r from-blue-500 to-purple-600 text-white px-3 py-1 rounded-full text-xs">
                Recommended
              </div>
              
              <div className="grid md:grid-cols-2 gap-6">
                {/* Flowchart Info */}
                <div className="flex flex-col justify-between">
                  <div>
                    <h3 className="text-gray-900 mb-2">{recommendedFlowchart.name}</h3>
                    <p className="text-sm text-gray-600 mb-4">{recommendedFlowchart.description}</p>
                  </div>
                  <Button
                    onClick={() => onSelectFlowchart(recommendedFlowchart)}
                    className="bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white w-full md:w-auto"
                  >
                    <Check className="w-4 h-4 mr-2" />
                    I prefer this flowchart
                  </Button>
                </div>

                {/* Flowchart Preview */}
                <div className="bg-white rounded-lg p-4 border border-gray-200 h-64">
                  {renderFlowchartPreview(recommendedFlowchart)}
                </div>
              </div>
            </div>
          </div>

          {/* Similar Flowcharts */}
          <div>
            <h3 className="text-gray-900 mb-4">Other Relevant Flowcharts</h3>
            <div className="grid md:grid-cols-3 gap-4">
              {similarFlowcharts.map((flowchart) => (
                <div
                  key={flowchart.id}
                  className="bg-white rounded-xl p-4 border border-gray-200 hover:border-purple-300 hover:shadow-lg transition-all"
                >
                  {/* Flowchart Preview */}
                  <div className="bg-gray-50 rounded-lg p-3 mb-3 h-40 border border-gray-100">
                    {renderFlowchartPreview(flowchart)}
                  </div>

                  {/* Flowchart Info */}
                  <div className="mb-3">
                    <h4 className="text-gray-900 mb-1">{flowchart.name}</h4>
                    <p className="text-xs text-gray-500 line-clamp-2">{flowchart.description}</p>
                  </div>

                  {/* Select Button */}
                  <Button
                    onClick={() => onSelectFlowchart(flowchart)}
                    variant="outline"
                    className="w-full text-sm border-purple-200 hover:bg-purple-50 hover:border-purple-300"
                  >
                    <Check className="w-3.5 h-3.5 mr-1.5" />
                    I prefer this flowchart
                  </Button>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
