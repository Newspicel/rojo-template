local game = remodel.readPlaceFile(".remodel/World.rbxl")

local workspace = game.Workspace

for _, content in ipairs(workspace:GetChildren()) do
	remodel.writeModelFile(content, "workspace/" .. content.Name .. ".rbxmx")
end