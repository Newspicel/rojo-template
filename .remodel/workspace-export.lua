local game = remodel.readPlaceFile(".remodel/place.rbxl")

local workspace = game.Workspace

for _, content in ipairs(workspace:GetChildren()) do
	remodel.writeModelFile(content, "workspace/" .. content.Name .. ".rbxm")
	print("Exported " .. content.Name .. " to workspace/" .. content.Name .. ".rbxm")
end
